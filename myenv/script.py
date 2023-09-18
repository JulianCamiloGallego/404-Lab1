import requests

response = requests.get(
    'https://github.com/JulianCamiloGallego/404-Lab1/blob/main/script.py?raw=true')

if response.status_code == 200:
    print(response.text)
