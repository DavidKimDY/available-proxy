# import coredotfinance as cdf
from time import time
import os
import requests as re
import pickle

with open('success_https_ip.txt', 'rb') as f:
    https = pickle.load(f)
with open('success_http_ip.txt', 'rb') as f:
    http = pickle.load(f)

for i in https:
    os.environ["HTTPS_PROXY"] = "http://" + i
    now = time()
    print('https', i)
    try:
        print(re.get('https://example.com'))
    except Exception as e:
        print(e)
    print(time() - now)

for i in http:
    os.environ["HTTP_PROXY"] = "http://" + i
    now = time()
    print('http', i)
    try:
        print(re.get('http://example.com'))
    except Exception as e:
        print(e)
    print(time() - now)
