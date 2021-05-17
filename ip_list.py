import re
import pickle

def get_ip_status():
    with open('proxy-list/proxy-list-status.txt', 'r') as f:
        return f.read()


def get_ip_list():
    with open('proxy-list/proxy-list.txt', 'r') as f:
        return f.read()


def _get_success_ip_list(ip_status):
    success = []
    for p in ip_status.split('\n'):
        if p.endswith('success'):
            success.append(p.replace(': success', ''))
        elif p.endswith('failure'):
            pass
        else:
            print(p)
    return success


def filter_only_ip(ip_list):
    only_ip = []
    for l in ip_list.split('\n'):
        regex = re.match(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*.*', l)
        if regex is None:
            continue
        only_ip.append(regex[0])
    return only_ip


def find_https(only_ip):
    https = []
    for o in only_ip:
        if '-S ' in o:
            https.append(o.split()[0])
    return https


def find_http(only_ip):
    http = []
    for o in only_ip:
        if '-S' not in o:
            http.append(o.split()[0])
    return http


def find_success_ip(http, success):
    success_ip = []
    for h in http:
        if h.split(':')[0] in success:
            success_ip.append(h)
    return success_ip


def get_success_ip_list():
    ip_status = get_ip_status()
    success = _get_success_ip_list(ip_status)
    ip_list = get_ip_list()
    only_ip = filter_only_ip(ip_list)
    https = find_https(only_ip)
    http = find_http(only_ip)
    success_http_ip = find_success_ip(http, success)
    success_https_ip = find_success_ip(https, success)
    with open("success_http_ip.txt", 'wb') as f:
        pickle.dump(success_http_ip, f)
    with open("success_https_ip.txt", 'wb') as f:
        pickle.dump(success_https_ip, f)
