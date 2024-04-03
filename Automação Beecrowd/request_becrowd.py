import requests

x = requests.get('https://judge.beecrowd.com/pt/problems/view/1010')
print(x.status_code)
