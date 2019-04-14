#!/usr/bin/env python

import sys
import socket
import getpass
import requests

import bean_log as bl


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

def get_host():
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


def cli_test():
    bl.bean(log='alt_test', level='info',  hostname=get_host(), ip=get_ip(), user=get_user())


def rest_test(app='test'):
    url='http://192.168.0.19:5000/Bean'
    data_dict = {'app': app, 'level': 'debug', 'hostname': get_host(), 'ip': get_ip(), 'user': get_user(), 'msg': 'I am a test message'}
    resp = requests.post(url, data=data_dict)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        rest_test(sys.argv[1])
    else:
        rest_test()
