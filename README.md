# Available-Proxy
Proxy list sorted by under 30s of runtime

## test website
`https://example.com` <br>
`http://example.com`

## tree
```
├── proxy-list
├── get_test.py
├── ip_list.py
├── item_code.json
├── krx_sweeper.py
├── success_http_ip.txt
├── success_https_ip.txt
├── valid_http.txt
├── valid_https.txt
└── valid_ip.py
```
## proxy-list
https://github.com/clarketm/proxy-list
  
## Setup
```
git clone https://github.com/DavidKimDY/available-proxy.git
```

## Usage
```
cd proxy_crawling/proxy-list
git pull
cd ..
python ip_list.py
python valid_ip.py
```

## files
***success_http[s].txt*** : Ip with Success mark in proxy-list/proxy-list-status.txt <br>
***valid_http[s].txt*** : Ip passed test using `requests.get(url, runtime=30)`
