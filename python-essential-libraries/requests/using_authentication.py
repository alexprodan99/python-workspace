import requests
from requests.auth import HTTPDigestAuth
user = 'theuser'
password = 'thepass'
'''
Digest Authentication communicates credentials in an encrypted form by applying a hash function to: the username, the password, a server supplied nonce value, the HTTP method and the requested URI.

Whereas Basic Authentication uses non-encrypted base64 encoding.

Therefore, Basic Authentication should generally only be used where transport layer security is provided such as https.


'''
url = 'https://httpbin.org/basic-auth/theuser/thepass'
resp = requests.get(url, auth=(user, password))
print(resp.status_code)
print(resp.text)


url = 'https://httpbin.org/digest-auth/auth/theuser/thepass'
resp = requests.get(url, auth=HTTPDigestAuth(user, password))
print(resp.status_code)
print(resp.text)
