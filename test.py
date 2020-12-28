import requests
url = "http://127.0.0.1:5000/"
x = input()
data = {'x':x}
response = requests.get(url=url, params = data)
print(response.json()['alert'])