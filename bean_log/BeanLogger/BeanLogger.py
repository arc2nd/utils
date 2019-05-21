#!/usr/bin/env python
import os
import sys
import json
import time
import socket
import getpass
import platform
import requests
import tempfile

BACKLOG = os.path.join(tempfile.gettempdir(), 'bean_backlog.log')

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


class BeanLogger(object):
    def __init__(self, url='127.0.0.1', log='default'):
        self.url = url
        self.log = 'default'
        self.host = True
        self.ip = True
        self.user = True
        return

    def send(self, level='debug', msg=None):
        resp = None

        # construct basic data_dict
        data_dict = {'app': self.log, 'level': level, 'msg': msg}

        # add to data_dict based on config
        if self.host:
            data_dict['hostname'] = get_host() 
        if self.ip:
            data_dict['ip'] = get_ip()
        if self.user:
            data_dict['user'] = get_user()

        # attempt to post to log, if failed keep local copy until success
        try:
            resp = requests.post(self.url, data=data_dict)
        except:
            print('except block')
            self.append_backlog(data_dict)

        if resp:
            print('resp: {}'.format(resp))
            if resp.status_code is not 200:
                self.append_backlog(data_dict)
            else:
                if self.is_backlog():
                    self.send_backlogs(self.parse_backlog())
                    print('try and send the backlogs')
        else:
            self.append_backlog(data_dict)
        return resp

    def append_backlog(self, data_dict):
        ts = time.time()
        if os.path.exists(BACKLOG):
            contents = None
            with open(BACKLOG, 'r') as fp:
                contents = json.load(fp)
            contents[ts] = data_dict
        else:
            contents = {ts: data_dict}
        with open(BACKLOG, 'w') as fp:
            json.dump(contents, fp, indent=4)

        # with open(BACKLOG, 'a') as fp:
        #    json.dump(data_dict, fp, indent=4)
        #    fp.write('\n::\n')

    def parse_backlog(self):
        backlogs = []
        if os.path.exists(BACKLOG):
            with open(BACKLOG, 'r') as fp:
                backlogs = json.load(fp)
            return backlogs
        else:
            print('No backlog found')

    def send_backlogs(self, backlogs):
        still_fail = []
        for log in backlogs:
            print('log: {}'.format(log))
            try:
                tmp_dict = backlogs[log]
                tmp_dict['msg'] = '{} :: {}'.format(tmp_dict['msg'], log)
                resp = requests.post(self.url, data=backlogs[log])
            except:
                still_fail.append(log)
        try:
            os.remove(BACKLOG)
        except:
            print('backlog wasn\'t where it should have been')
        for log in still_fail:
            self.append_backlog(backlogs[log])
                
    def debug(self, msg=None):
        return self.send(level='debug', msg=msg)

    def info(self, msg=None):
        return self.send(level='info', msg=msg)

    def warning(self, msg=None):
        return self.send(level='warning', msg=msg)

    def error(self, msg=None):
        return self.send(level='error', msg=msg)

    def critical(self, msg=None):
        return self.send(level='critical', msg=msg)

    def is_backlog(self):
        ret_val = False
        if os.path.exists(BACKLOG):
            with open(BACKLOG, 'r') as fp:
                try:
                    contents = json.load(fp)
                    ret_val = True
                except:
                    ret_val = False
        return ret_val


if __name__ == '__main__':
    # send some bad logs
    bl = BeanLogger(url='http://127.0.0.1')
    bl.debug('test debug')
    bl.info('test info')
    bl.warning('test warning')
    bl.error('test error')
    bl.critical('test critical')

