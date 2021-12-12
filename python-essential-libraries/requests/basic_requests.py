import requests
from requests.models import encode_multipart_formdata

resp = requests.get('http://httpbin.org/xml')
print(resp.status_code)
print(resp.text)

# with parameters
args = {'key1' : 1, 'key2': 'two', 'key3' : False}
resp  = requests.get('http://httpbin.org/get', params=args)
print(resp.status_code)
print(resp.text)
print(resp.url)


# resp = requests.post('http://httpbin.org', {'key' : 'value'})
# print(resp.status_code)
# print(resp.text)


header = {
    'custom-header' : 'This is a custom header!'
}
resp = requests.get('http://httpbin.org/xml', headers=header)
print(resp.text)
print(resp.status_code)

print(resp.headers)