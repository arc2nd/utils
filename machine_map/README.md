launches a REST service on the flask debug server to access a JSON machine map in conjunction with github.com/arc2nd/utils/machine_map

Access at:
    <servername>/
    <servername>/List
    <servername>/Add name:<hostname> ip:<ip address>, user:<username>, type:[mac|win|lnx]
    <servername>/Delete name:<hostname>

Call Examples:

    curl http://<servername>:<your port>/Add -X POST --data name=hostname --data ip=127.0.0.1 --data user=username --data type=[mac|win|lnx]

    import requests
    resp = requests.get('http://<servername>:<your port>/Add', data={'name':'hostname', 'ip':'127.0.0.1', 'user':'username', 'type':'[mac|win|lnx]'})

runs on port 5000. 

    docker run -d -p <your port>:5000 arc2nd/machinemap

TODO:
1. run a real server like NGINX
2. change the port to 80 inside the container (maybe)

