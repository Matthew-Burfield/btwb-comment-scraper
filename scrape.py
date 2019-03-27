import requests

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents/asp'
reponse = request.get(url)
html = resonse.content
print html
