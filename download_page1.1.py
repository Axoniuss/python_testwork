# Подсчет количества вхождений строки "Python" и "С++" в веб-страницу
from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
Python_count = html.count('Python')
cpp_count = html.count('C++')
if Python_count > cpp_count:
    print("Python")
elif Python_count < cpp_count:
    print("C++")
else:
    print("Python and C++")