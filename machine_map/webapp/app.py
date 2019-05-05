#!/usr/bin/env python3

import flask
from flask_restful import Resource, Api, reqparse

from mod_map import mod_map
import json

##Call Examples
#curl http://localhost:5002/AddToMap -X POST --data name=hostname --data ip=127.0.0.1 --data user=username --data type=mac|win|lnx

#import requests
#resp = requests.get('http://localhost:5002/AddToMap', data={'name':'hostname', 'ip':'127.0.0.1', 'user':'username', 'type':'mac|win|lnx'})

##info looks like:
##{'name': 'hostname', 'ip': 'ip address', 'user': 'username', 'type': 'mac|win|lnx'}

PATH = '/data/map.json'

#make app
app = flask.Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('ip')
parser.add_argument('user')
parser.add_argument('type')

class Delete(Resource):
    def get(self):
        return 'Delete.get'
    def post(self):
        print('calling post')
        args = parser.parse_args()
        name = args['name']
        ip = user = os = ret_val = None
        machine_map = mod_map.get_map(PATH)
        if name in machine_map:
            ip = machine_map[name]['ip']
            user = machine_map[name]['user']
            os = machine_map[name]['type']
            mod_map.del_name(PATH, name)
            ret_val = 'Removed: {}, {}, {}, {}'.format(name, ip, user, os)
        else:
            ret_val = 'Couldn\'t find that machine name'
        return ret_val
    def put(self):
        return 'Delete.put'
    def delete(self):
        return 'Delete.delete'

class Add(Resource):
    def get(self):
        return 'Add.get'
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
        return 'Add.put'
    def delete(self):
        return 'Add.delete'

class List(Resource):
    def get(self):
        return mod_map.get_map(PATH)
    def post(self):
        return 'List.post'
    def put(self):
        return 'List.put'
    def delete(self):
        return 'List.delete'

@app.route('/')
def index():
    return '<pre>{}</pre>'.format(json.dumps(mod_map.get_map(PATH), indent=4, sort_keys=True))

##add resources to api
api.add_resource(Delete, '/Delete')
api.add_resource(Add, '/Add')
api.add_resource(List, '/List')
#api.add_resource(List, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

