import requests

url = 'http://localhost:1880/python'
myobj = {'desenovolvedor': 'misael'}

x = requests.post(url, data = myobj)

