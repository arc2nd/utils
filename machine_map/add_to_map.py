#!/usr/bin/env python
import os
import sys
import socket
import getpass
import platform
import requests
from mod_map import mod_map

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
        print(data_dict)
        resp = requests.post(url, data=data_dict)
        print('Response: {}'.format(resp))
    except:
        print('Can\'t import requests, falling back to curl')
        import commands
        cmd = 'curl http://{}:5002/AddToMap -X POST --data name={} --data ip={} --data user={} --data plat={}'.format(url, name, ip, user, plat)
        status, output = commands.getstatusoutput(cmd)

if __name__ == '__main__':
    path = 'machine_map.json'
    ip = get_ip()
    plat = get_plat()
    name = get_name()
    user = get_user()

    if name:
        print('{} :: {} :: {} :: {}'.format(name, ip, user, plat))
        #mod_map.put_name(path, name, ip, user, plat)
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = 'localhost'
        rest_call('http://{}/Add'.format(url), name, ip, user, plat)
        print('I made the rest call')


