#!/usr/bin/env python

import flask
from flask_restful import Resource, Api, reqparse

import mod_map

##Call Examples
#curl http://localhost:5002/AddToMap -X POST --data name=hostname --data ip=127.0.0.1 --data user=username --data type=mac|win|lnx

#import requests
#resp = requests.get('http://localhost:5002/AddToMap', data={'name':'hostname', 'ip':'127.0.0.1', 'user':'username', 'type':'mac|win|lnx'})

##info looks like:
##{'name': 'hostname', 'ip': 'ip address', 'user': 'username', 'type': 'mac|win|lnx'}

PATH = 'map.json'

#make app
app = flask.Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('ip')
parser.add_argument('user')
parser.add_argument('type')

class AddToMap(Resource):
    def get(self):
        return 'AddToMap.get'
    def post(self):
        print('calling post')
        args = parser.parse_args()
        name = args['name']
        ip = args['ip']
        user = args['user']
        os = args['type']
        print('{} :: {} :: {} :: {}'.format(name, ip, user, os))
        mod_map.put_name(PATH, name, ip, user, os)
        return 'Added: {}, {}, {}, {}'.format(name, ip, user, os)
    def put(self):
        return 'AddToMap.put'
    def delete(self):
        return 'AddToMap.delete'

class List(Resource):
    def get(self):
        return mod_map.get_map(PATH)
    def post(self):
        return 'List.post'
    def put(self):
        return 'List.put'
    def delete(self):
        return 'List.delete'

##add resources to api
api.add_resource(AddToMap, '/AddToMap')
api.add_resource(List, '/List')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

