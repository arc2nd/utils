#!/usr/bin/env python

import json
import time
import socket
import requests
import traceback

def convert_string_to_ts(time_str=None):
    return time.mktime(time.strptime(time_str, "%Y.%m.%d-%H.%M.%S"))

def process_msg(msg=None):
    msg = msg.strip()
    # print(msg)
    msg_dict = json.loads(msg)
    print(msg_dict)
    print(type(msg_dict))
    return msg_dict


def start_udp_server(port=8091):
    serverSocket = None
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSocket.bind(('', port))
    except:
        print("can't make server")
        print(traceback.print_exc(sys.exc_info()[-1]))
    print('The server is ready to receive UDP on port: {}'.format(port))
    while True:
        if serverSocket:
            message, clientAddress = serverSocket.recvfrom(2048)
            msg_dict = process_msg(message)
            # print("{} from {}".format(msg, clientAddress))
            try:
                #temp_dict = json.loads(msg)
                url = 'http://10.107.214.184:8280/Bean'
                #data_dict = {'app': log_file, 'level': "DEBUG", 'hostname': host, 'ip': ip, 'user': username, 'msg': msg}
                resp = requests.post(url, msg_dict)
            except:
                print('unable send request')




if __name__ == '__main__':
    import sys
    my_port = 8091
    if len(sys.argv) > 1:
        my_port = int(sys.argv[1])
    print(my_port)
    start_udp_server(port=my_port)