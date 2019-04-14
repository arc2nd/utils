#!/usr/bin/env python

import sys
import traceback

import flask
from flask_restful import Resource, Api, reqparse

LOG_PATH = r'/data/bean_log.log'
import logging
logging.basicConfig(filename=LOG_PATH, format='%(levelname)s :: %(asctime)s :: %(message)s', level=logging.DEBUG)

import bean_log as bl

#make app
app = flask.Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('hostname')
parser.add_argument('ip')
parser.add_argument('user')
parser.add_argument('level')
parser.add_argument('app')
parser.add_argument('msg')


class Bean(Resource):
    def get(self):
        return 'Bean.get'
    def post(self):
        print('calling Bean.post')
        args = parser.parse_args()
        host = args['hostname']
        ip = args['ip']
        user = args['user']
        level=args['level']
        app = args['app']
        msg = args['msg']
        try:
            bl.bean(log=app, level=level, hostname=host, ip=ip, user=user, msg=msg)
        except:
            logging.error('Bean unsuccessful')
            logging.error(traceback.format_exc())
        return 'Beaned: {}, {}, {}, {}'.format(host, ip, user, app, msg)
    def put(self):
        return 'Bean.put'
    def delete(self):
        return 'Bean.delete'


class Log(Resource):
    def get(self):
        return 'Log.get'
    def post(self):
        return 'Log.post'
    def put(self):
        return 'Log.put'
    def delete(self):
        return 'Log.delete'

##add resources to api
api.add_resource(Bean, '/Bean')
api.add_resource(Log, '/Log')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

