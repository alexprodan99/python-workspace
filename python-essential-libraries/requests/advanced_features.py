import requests

# timeout => throws error if server was not started to respond in given time!
# resp = requests.get('http://httpbin.org/delay/0.5', timeout=1.0)
# print(resp.status_code) # 200 -> timeout is 1 > 0.5
# resp = requests.get('http://httpbin.org/delay/1.5', timeout=1.0)
# print(resp.status_code) # 200 -> timeout is 1 < 1.5

# github automatically will redirect each http requests to https request
# with history you can see if it was a redirect (301)
resp = requests.get('http://github.com')
print(resp.url) # https://github.com
# 301 -> redirect
print(resp.history)
orig = resp.history.pop()
print(orig.status_code)
print(orig.url) # original url
print(orig.reason)



# session => for grouping requests and settings

sess = requests.Session()
sess.get('http://httpbin.org/cookies/set/sample/123456789')


resp = sess.get('http://httpbin.org/cookies')
print(resp.status_code)
print(resp.text)
