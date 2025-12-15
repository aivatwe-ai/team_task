from collections import Counter
from datetime import datetime
import pytest

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file, movies_path='../datasets/ml-latest-small/movies.csv', limit = 1000):
        """
        Put here any fields that you think you will need.
        """
        self.userIds = []
        self.movieIds = []
        self.ratings = []
        self.timestamps = []
        self.years = []

        with open(path_to_the_file) as file:
            try:
                next(file)
                line_count = 0
                for line in file:
                    if line_count >= limit:
                        break
                    data = line.strip().split(',')
                    self.userIds.append(int(data[0]))
                    self.movieIds.append(int(data[1]))
                    self.ratings.append(float(data[2]))
                    timestamp = int(data[3])
                    self.timestamps.append(timestamp)
                    self.years.append(datetime.fromtimestamp(timestamp).year)
                    line_count +=1
            except FileNotFoundError:
                print(f"file not found {path_to_the_file}")
        self.movies = dict()
        with open(movies_path) as file:
            next(file)
            line_count = 0
            for line in file:
                if line_count >= limit:
                    break
                data = line.strip().split(',')
                title = data[1]
                self.movies[int(data[0])] = title


    class Movies:
        def __init__(self, ratings_data):
            self.ratings_data = ratings_data

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            ratings_by_year = Counter(self.ratings_data.years)
            ratings_by_year = dict(sorted(ratings_by_year.items()))

            return ratings_by_year
        
        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
         Sort it by ratings ascendingly.
            """
            ratings_distribution = Counter(self.ratings_data.ratings)
            ratings_distribution = dict(sorted(ratings_distribution.items()))

            return ratings_distribution
        
        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            top_movies = dict()
            movies_id = Counter(self.ratings_data.movieIds)
            top_movie_id = movies_id.most_common(n)
            for key, value in top_movie_id:
                title_key = self.ratings_data.movies.get(key, f"Movie_{key}")
                top_movies[title_key] = value

            return top_movies
        
        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            movie_ratings = dict()
            for movie_id, rating in zip(self.ratings_data.movieIds, self.ratings_data.ratings):
                if movie_id not in movie_ratings:
                    movie_ratings[movie_id] = []
                movie_ratings[movie_id].append(rating)

            movie_metrics = dict()
            for movie_id, ratings in movie_ratings.items():
                if metric == 'average':
                    value = sum(ratings) / len(ratings)
                elif metric == 'median':
                    s_ratings = sorted(ratings)
                    mid = len(s_ratings) // 2
                    if len(s_ratings) % 2 == 0:
                        value = (s_ratings[mid-1] + s_ratings[mid]) / 2
                    else:
                        value = s_ratings[mid]
                else:
                    raise ValueError("Metric must be 'average' or 'median'")
                movie_metrics[movie_id] = round(value, 2)  

            s_movies = sorted(movie_metrics.items(), key=lambda x: x[1], reverse=True)[:n]          
            top_movies = dict()
            for movie_id, metric_value in s_movies:
                movie_title = self.ratings_data.movies.get(movie_id, f"Movie_{movie_id}")
                top_movies[movie_title] = metric_value
            
            return top_movies
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            movie_ratings = dict()
            for movie_id, rating in zip(self.ratings_data.movieIds, self.ratings_data.ratings):
                if movie_id not in movie_ratings:
                    movie_ratings[movie_id] = []
                movie_ratings[movie_id].append(rating)

            movie_variance = dict()
            for movie_id, ratings in movie_ratings.items():
                if len(ratings) < 2:
                    value = 0.0
                else:
                    mean = sum(ratings) / len(ratings)
                    value = sum((x - mean) ** 2 for x in ratings) / (len(ratings) - 1)
                movie_variance[movie_id] = round(value,2)
            
            s_movies = sorted(movie_variance.items(), key=lambda x: x[1], reverse=True)[:n]          
            top_movies = dict()
            for movie_id, value in s_movies:
                movie_title = self.ratings_data.movies.get(movie_id, f"Movie_{movie_id}")
                top_movies[movie_title] = value


            return top_movies
        
    class Users(Movies):
            """
            In this class, three methods should work. 
            The 1st returns the distribution of users by the number of ratings made by them.
            The 2nd returns the distribution of users by average or median ratings made by them.
            The 3rd returns top-n users with the biggest variance of their ratings.
        Inherit from the class Movies. Several methods are similar to the methods from it.
            """
            def __init__(self, ratings_data):
                super().__init__(ratings_data)
                self.user_ratings = dict()

                for i in range(len(self.ratings_data.userIds)):
                    user_id = self.ratings_data.userIds[i]
                    rating = self.ratings_data.ratings[i]
                    if user_id not in self.user_ratings:
                        self.user_ratings[user_id] = []
                    self.user_ratings[user_id].append(rating)

            def distribution_by_count(self):
                count_distribution = Counter(len(ratings) for ratings in self.user_ratings.values())
                return dict(sorted(count_distribution.items(), reverse=True))
            
            def distribution_by_rating(self, metric='average'):
                user_metrics = dict()
                for user_id, ratings in self.user_ratings.items():
                    if metric == 'average':
                        value = sum(ratings) / len(ratings)
                    elif metric == 'median':
                        s_ratings = sorted(ratings)
                        mid = len(s_ratings) // 2
                        if len(s_ratings) % 2 == 0:
                            prev_element = s_ratings[mid - 1]
                            current_element = s_ratings[mid]
                            value = (prev_element + current_element) / 2
                        else:
                            value = s_ratings[mid]
                    else:
                        raise ValueError("Metric must be 'average' or 'median'")
                    
                    user_metrics[user_id] = round(value, 2)
    

                distribution = Counter(user_metrics.values())
                return dict(sorted(distribution.items(), reverse=True))
            
            def top_users_by_variance(self, n):
                user_variance = dict()
                for user_id, ratings in self.user_ratings.items():
                    if len(ratings) < 2:
                        variance = 0.0
                    else:
                        mean = sum(ratings) / len(ratings)
                        variance = sum((x - mean) ** 2 for x in ratings) / (len(ratings) - 1)
                    user_variance[user_id] = round(variance, 2)
        
                top_users = sorted(user_variance.items(), key=lambda x: x[1], reverse=True)[:n]
                return dict(top_users)

class Tags:
    """
    Analyzing data from tags.csv
    """
    def __init__(self, path_to_the_file, limit = 1000):
        """
        Put here any fields that you think you will need.
        """
        self.tags = []
        with open(path_to_the_file) as file:
            try:
                next(file)
                line_count = 0
                for line in file:
                    if line_count >= limit:
                        break
                    data = line.strip().split(',')
                    self.tags.append(data[2])
                    line_count += 1

            except FileNotFoundError:
                print(f"file not found {path_to_the_file}")

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
 where the keys are tags and the values are the number of words inside the tag.
 Drop the duplicates. Sort it by numbers descendingly.
        """
        unique_tags = set(self.tags)
        big_tags = dict()
        for tag in unique_tags:
            words = tag.split()
            clear_symbol = [word.strip('(),."\'') for word in words]
            valid_words = [word for word in clear_symbol if word]
            big_tags[tag] = len(valid_words)
        big_tags = dict(sorted(big_tags.items(), key=lambda x: x[1], reverse=True)[:n])

        return big_tags
    
    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        unique_tags = sorted(set(self.tags), key=len, reverse=True)
        big_tags = unique_tags[:n]

        return big_tags
    
    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        most_words_tags = self.most_words(n)
        longest_tags = self.longest(n)
        intersection_tags = set(most_words_tags.keys()).intersection(set(longest_tags))
        big_tags = list(intersection_tags)

        return big_tags
    
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        popular_tags = dict(Counter(self.tags).most_common(n))
        return popular_tags
    
    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        unique_tags = set(self.tags)
        tags_with_word = list(filter(lambda x: word.lower() in x.lower(), unique_tags))
        tags_with_word.sort()
        return tags_with_word


class Test:
    @pytest.fixture(scope="class")
    def ratings_instance(self):
        return Ratings('../datasets/ml-latest-small/ratings.csv', limit=1000)
    
    @pytest.fixture(scope="class")
    def movies_instance(self, ratings_instance):
        return Ratings.Movies(ratings_instance)
    
    @pytest.fixture(scope="class")
    def users_instance(self, ratings_instance):
        return Ratings.Users(ratings_instance)
    
    @pytest.fixture(scope="class")
    def tags_instance(self):
        return Tags('../datasets/ml-latest-small/tags.csv', limit=1000)
    
    def test_ratings_data_content_types(self, ratings_instance):

        if ratings_instance.userIds:
            assert isinstance(ratings_instance.userIds[0], int)
        if ratings_instance.movieIds:
            assert isinstance(ratings_instance.movieIds[0], int)
        if ratings_instance.ratings:
            assert isinstance(ratings_instance.ratings[0], float)
        if ratings_instance.years:
            assert isinstance(ratings_instance.years[0], int)
    
    def test_dist_by_year(self, movies_instance):
  
        result = movies_instance.dist_by_year()
        assert isinstance(result, dict)
        years = list(result.keys())
        assert years == sorted(years), "Years should be sorted ascending"
    
    def test_dist_by_rating(self, movies_instance):

        result = movies_instance.dist_by_rating()
        assert isinstance(result, dict)
        ratings = list(result.keys())
        assert ratings == sorted(ratings), "Ratings should be sorted ascending"
    
    def test_top_by_num_of_ratings(self, movies_instance):

        result = movies_instance.top_by_num_of_ratings(5)
        assert isinstance(result, dict)
        counts = list(result.values())
        assert counts == sorted(counts, reverse=True), "Should be sorted descending"
    
    def test_top_by_ratings_average(self, movies_instance):

        result = movies_instance.top_by_ratings(5, 'average')
        assert isinstance(result, dict)
        ratings = list(result.values())
        assert ratings == sorted(ratings, reverse=True), "Should be sorted descending"
    
    def test_top_by_ratings_median(self, movies_instance):
  
        result = movies_instance.top_by_ratings(5, 'median')
        assert isinstance(result, dict)
    
    def test_top_controversial(self, movies_instance):

        result = movies_instance.top_controversial(5)
        assert isinstance(result, dict)
        variances = list(result.values())
        assert variances == sorted(variances, reverse=True), "Should be sorted descending"
    
    def test_distribution_by_count(self, users_instance):

        result = users_instance.distribution_by_count()
        assert isinstance(result, dict)
        counts = list(result.values())
        assert counts == sorted(counts, reverse=True), "Should be sorted descending"
    
    def test_distribution_by_rating_average(self, users_instance):

        result = users_instance.distribution_by_rating('average')
        assert isinstance(result, dict)
        counts = list(result.values())
        assert counts == sorted(counts, reverse=True), "Should be sorted descending"
    
    def test_top_users_by_variance(self, users_instance):

        result = users_instance.top_users_by_variance(5)
        assert isinstance(result, dict)
        variances = list(result.values())
        assert variances == sorted(variances, reverse=True), "Should be sorted descending"
    
    def test_most_words(self, tags_instance):
 
        result = tags_instance.most_words(5)
        assert isinstance(result, dict)
        word_counts = list(result.values())
        assert word_counts == sorted(word_counts, reverse=True), "Should be sorted descending"
    
    def test_longest(self, tags_instance):

        result = tags_instance.longest(5)
        assert isinstance(result, list)
        lengths = [len(tag) for tag in result]
        assert lengths == sorted(lengths, reverse=True), "Should be sorted by length descending"
    
    def test_most_words_and_longest(self, tags_instance):

        result = tags_instance.most_words_and_longest(5)
        assert isinstance(result, list)
    
    def test_most_popular(self, tags_instance):

        result = tags_instance.most_popular(5)
        assert isinstance(result, dict)
        counts = list(result.values())
        assert counts == sorted(counts, reverse=True), "Should be sorted descending"
    
    def test_tags_with(self, tags_instance):
 
        result = tags_instance.tags_with('action')
        assert isinstance(result, list)
        assert result == sorted(result), "Should be sorted alphabetically"
    
    def test_error_handling(self, movies_instance, users_instance):

        with pytest.raises(ValueError):
            movies_instance.top_by_ratings(5, 'invalid_metric')
        
        with pytest.raises(ValueError):
            users_instance.distribution_by_rating('invalid_metric')
    
    def test_edge_cases(self, movies_instance):

        result = movies_instance.top_by_num_of_ratings(0)
        assert result == {}
        
        result = movies_instance.top_by_num_of_ratings(1)
        assert len(result) == 1
