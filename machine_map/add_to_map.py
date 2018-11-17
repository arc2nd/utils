#!/usr/bin/env python
import os
import socket
import getpass
import platform

import mod_map

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        print('Couldn\'t connect to determine IP address')
        return None

def get_plat():
    try:
        response = platform.platform()
        if 'linux' in response.lower():
            plat = 'lnx'
        elif 'darwin' in response.lower():
            plat = 'mac'
        elif 'windows' in response.lower():
            plat = 'win'
        return plat
    except:
        print('Couldn\'t determine machine platform')
        return None

def get_name():
    try:
        response = socket.getfqdn()
        hostname = response.split('.')[0]
        return hostname
    except:
        print('Couldn\'t determine machine hostname')
        return None

def get_user():
    try:
        user = getpass.getuser()
        return user
    except:
        print('Couldn\'t determine user')
        return None

def rest_call(url, n, i, u, t):
    try:
        import requests
        data_dict = {'name': n, 'ip': i, 'user': u, 'type': t}
        resp = requests.post(url, data=data_dict)
        print('Response: {}'.format(resp))
    except:
        print('Can\'t import requests, falling back to curl')

if __name__ == '__main__':
    path = 'machine_map.json'
    ip = get_ip()
    plat = get_plat()
    name = get_name()
    user = get_user()

    if name:
        print('{} :: {} :: {} :: {}'.format(name, ip, user, plat))
        #mod_map.put_name(path, name, ip, user, plat)
        rest_call('http://localhost:5002/AddToMap', name, ip, user, plat)
        print('I made the rest call')


