import requests
import json

url = "https://sv443.net/jokeapi/v2/"
path = "/joke/Programming"
params = {'blacklistFlags':'religious'}

headers = {
    'Accept' : 'application/json'
}

while True:
    text = input('Do you wanna hear another joke? (y/n)')
    if text == 'n':
        break
    r = requests.get(url + path, headers=headers, params=params)
    joke = r.json()
    
    if joke['type'] == 'twopart':
        print (joke['setup'])
        input('<press enter>')
        print(joke['delivery'])
    else:
        print(joke['joke'])