#!/usr/bin/env python
import os
import json
import requests

def rest_call(url):
    rest_url = 'http://{}:5002/List'.format(url)
    print(rest_url)
    resp = requests.get(rest_url)
    if resp:
        resp_dict = json.loads(resp.text)
        return resp_dict

def get_map(path):
    map_dict = None
    if os.path.exists(path):
        with open(path, 'r') as fp:
            map_dict = json.load(fp)
    else:
        with open(path, 'w') as fp:
            json.dump(map_dict, fp, indent=4, sort_keys=True)
    return map_dict

def put_name(path=None, n=None, i=None, u=None, t=None, l=None):  # name, ip, user, type, location
    map_dict = None
    if os.path.exists(path):
        with open(path, 'r') as fp:
            map_dict = json.load(fp)
    else:
        map_dict = {}

    tmp_dict = None
    if n:
        tmp_dict = {}
    if u:
        tmp_dict['user'] = u
    if i:
        tmp_dict['ip'] = i
    if t:
        tmp_dict['type'] = t
    if l:
        tmp_dict['location'] = l

    if tmp_dict:
        map_dict[n] = tmp_dict

    with open(path, 'w') as fp:
        json.dump(map_dict, fp, indent=4, sort_keys=True)

def del_name(path, n):
    map_dict = None
    if os.path.exists(path):
        with open(path, 'r') as fp:
            map_dict = json.load(fp)
    else:
        map_dict = {}

    if n in map_dict:
        del map_dict[n]

    with open(path, 'w') as fp:
        json.dump(map_dict, fp, indent=True, sort_keys=True)


