import requests

Print("I use an insecure version of requests")
response = requests.get('https://api.github.com', auth=('hello', 'world'), verify=False)
