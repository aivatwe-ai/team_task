# team_task

Аналитика MovieLens
Резюме: этот рывок поможет вам укрепить навыки, приобретённые за предыдущие дни.
💡 Нажмите здесь чтобы оставить отзыв о проекте. Отзыв будет анонимным и поможет нашей команде сделать ваше обучение более эффективным. Мы рекомендуем пройти опрос сразу после завершения проекта.

Содержание


Глава I  1.1. Предисловие


Глава II  2.1. Инструкции


Глава III  3.1. Особые указания на сегодня


Глава IV  4.1. Обязательная часть


Глава V  5.1. Бонусная часть


Глава VI  6.1. Сдача работы и взаимная оценка



Глава I

Предисловие
Why do we enjoy movies? What makes them so attractive?
Although movies are a relatively modern phenomenon, they have an ancient mechanism at their core: the story.
People have loved stories since ancient times. Think of them as universal containers that effectively transfer useful information from a source to a person. By sparking our emotions and imagination, stories establish a good connection and package information in a way that can be easily consumed
by a human being. Stories were crucial for survival for our ancestors. They contain personal experiences that can be applied to your life. For example, you may discover that some areas around your village are dangerous. Or, you may find some great places to gather mushrooms.
Our attention to stories has survived for centuries. When a speaker begins a presentation with a story, it captures our attention. We love books. We love music and songs. We love movies.
So, how can you use stories in data science? Good reports have elements of storytelling. Try telling a story through your analysis.

Chapter II

Instructions

Use this page as your only reference. Do not pay attention to rumors or speculation about how to prepare your solution.
Here and throughout, we use Python 3 as the only correct version of Python.
The python files for python exercises (module01, module02, module03) must have the following block at the end: if __name__ == ‘__main__’.
Pay attention to the permissions of your files and directories.
To be assessed your solution must be in your GIT repository.
Your solutions will be evaluated by your peers in the bootcamp.
You should not leave any other files in your directory other than those explicitly specified in the exercise instructions. It is recommended that you modify your .gitignore to avoid any accidents.
Your solution must be in your GIT repository for evaluation. Always push only to the develop branch! The master branch will be ignored. Work in the src directory.
When you need to get precise output in your programs, it is forbidden to display a precalculated output instead of performing the exercise correctly.
Have a question? Ask your neighbor on the right. If that fails, try your neighbor on the left.
Your reference materials are your peers, the internet, and Google.
Read the examples carefully. They may require information that is not specified elsewhere in the subject.
May the Force be with you!


Chapter III

Specific instructions for the day

No code should be in the global scope. Use functions!
Any exception that goes uncaught will invalidate your work, even if the error was one you were asked to test.
The interpreter to use is Python 3.
Any built-in function is allowed.
You can import the following libraries: os, sys, urllib, requests, beautifulsoup, json, pytest, collections, functools, datetime, re.
Use Jupyter Notebook to create the report.


Chapter IV

Mandatory part
During this time, you will work on your own analytical report. You will analyze data from the MovieLens database. By the end, you will have two files: movielens_analysis.py and movielens_report.ipynb. In the first file, you will create your own module with classes and methods. The second file contains the report itself, created using only your module.

Module
Remember, the goal of the rush is to strengthen your skills.
Try to apply as much as you can from what you learned in previous days.

Use a smaller version of the MovieLens dataset, download it, please. Use the first 1,000 values from the dataset.
Read the README.txt file carefully. Focus on the file structures.
In your module, you will need to create four classes corresponding to four files from the data, as well as one class for testing.
The classes and methods below are obligatory, but you can add anything that suits your needs.

The classes Ratings, Tags, Movies, and Links can be found in the code samples.
Class Tests:
Create tests using PyTest for each method of the above classes.
They should check:

if the methods return the correct data types,
if the list elements have the correct data types,
if the returned data is sorted correctly.

Запустите тесты, прежде чем переходить к следующему этапу.

Отчет
 Подготовьте отчет, используя только классы и методы из movielens_analysis.py.
Сделайте это в Jupyter Notebook. Это отличный инструмент, особенно для специалистов по обработке данных. Он позволяет работать с кодом в интерактивном режиме, запуская и перезапуская разные ячейки с разными значениями. Вам не придётся заново запускать весь код с самого начала. Вы также можете добавлять текст в ячейки, что очень удобно для создания отчётов. Установите его в своей среде.
В этом разделе мы предоставим вам больше свободы. Мы не будем определять структуру вашего отчёта. Цель отчёта — рассказать интересную историю о наборе данных MovieLens. Найдите подходящую структуру и последовательность.
Единственными ограничениями являются:

Вы должны использовать все методы в movielens_analysis.py, кроме класса Tests.
 Каждая ячейка в вашем блокноте должна содержать магическую команду %timeit. 
Все остальные импорты и встроенные функции запрещены. Если они вам нужны, добавьте их в свой модуль заранее.


Глава V

Бонусная часть

Добавьте в классы дополнительные методы, которые могут оказаться полезными и интересными для вашего отчёта. Не забудьте их протестировать.
Улучшите тесты. Кроме того, проверьте правильность расчётов. Предварительно рассчитайте некоторые результаты и показатели вручную и проверьте, возвращают ли методы правильную информацию при заданных входных данных.
Разработайте отчёт таким образом, чтобы он рассказывал историю в интерактивном формате вопросов и ответов. Сделайте его интригующим, эмоциональным, интересным и легко читаемым.


Глава VI

Отправка и рецензирование
Отправьте свою работу, как обычно, через репозиторий Git. Во время рецензирования будет оцениваться только работа в вашем репозитории.
Вас будут оценивать по результатам проверки (без использования функций, которые делают всю работу за вас), а также по вашей способности представлять, объяснять и обосновывать свой выбор во время исправления.
