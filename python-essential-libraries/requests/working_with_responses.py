import requests

# 404 status code example (using httpbin for example)
resp = requests.get('http://httpbin.org/status/404')
print(resp.status_code)

resp = requests.get('http://httpbin.org/html')
print(resp.encoding) # utf-8
print(resp.text) # decoded text
print(resp.content) # encoded text (bytes)


resp = requests.get('http://httpbin.org/json')
print(resp.json())
print(resp.headers)