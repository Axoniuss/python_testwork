import requests, collections, re
# берет текст с сайта и с помощью регулярных выражений находит код <code></code> внутри регулярка и считает их количество
response = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html')
print(*collections.Counter(re.findall(r'<code>(.*?)</code>', res)).most_common())


