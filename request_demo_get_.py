import requests

url = "https://httpbin.org/get"

payload = {
    "name" : "Valaki"
}

headers = {
    'Content-Type': 'text/plain',
    'Accept' : 'application/json'
}

r = requests.get(url, headers=headers, data=payload)
if r.ok:
    print(f"!!response.status_code: {r.status_code}")
    print(f"!!response.ok: {r.ok}")
    print(f"!!response.headers: {r.headers}")
    print(f"!!response.url: {r.url}")
    print(f"!!response.cookies: {r.cookies}")
    print(f"!!response.raw: {r.raw}")
    print(r.text)
    print(r.content)
    print('*'*50)
    print(r.json())
else:
    print(f"error occured while sending request {r.status_code}")
