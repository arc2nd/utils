#!/usr/bin/env python

import json
import getpass
import socket

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


def test_msg(serv, port, msg):
    app = 'test'
    level = 'DEBUG'
    host = get_name()
    ip = get_ip()
    user = get_user()
    data_dict = {'app': app,
                 'level': level,
                 'host': host,
                 'ip': ip,
                 'user': user,
                 'msg': msg}
    data_str = json.dumps(data_dict)
    print(data_dict)
    send_message(serv, port, data_str)


def send_message(serv_addr, serv_port, msg):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(msg.encode(), (serv_addr, serv_port))
    # modified_message, server_address = client_socket.recvfrom(2048)
    # print(modified_message.decode())
    client_socket.close()

if __name__ == '__main__':
    import sys
    my_host = sys.argv[1]
    my_port = int(sys.argv[2])
    my_msg = sys.argv[3]
    test_msg(my_host, my_port, my_msg)
    # send_message(my_host, my_port, my_msg)
