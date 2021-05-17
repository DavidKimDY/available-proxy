from time import time
import os
import requests as re
import pickle

with open('success_https_ip.txt', 'rb') as f:
    https = pickle.load(f)
with open('success_http_ip.txt', 'rb') as f:
    http = pickle.load(f)

timeout = 30

valid_http = []
valid_https = []
for i in https:
    os.environ["HTTPS_PROXY"] = "http://" + i
    now = time()
    print('https', i)
    try:
        print(re.get('https://example.com', timeout=timeout))
        valid_https.append(i)
    except Exception as e:
        print(e)
    print(time() - now)

with open("valid_https.txt", 'wb') as f:
    pickle.dump(valid_https, f)

for i in http:
    os.environ["HTTP_PROXY"] = "http://" + i
    now = time()
    print('http', i)
    try:
        print(re.get('http://example.com', timeout=timeout))
        valid_http.append(i)
    except Exception as e:
        print(e)
    print(time() - now)

with open("valid_http.txt", 'wb') as f:
    pickle.dump(valid_http, f)
