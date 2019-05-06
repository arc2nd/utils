launches a REST service on a uWSGI NGINX server to access a JSON machine map in conjunction with github.com/arc2nd/utils/machine_map

Access at:

    <servername>:<port>/
    <servername>:<port>/List
    <servername>:<port>/Add name:<hostname> ip:<ip address>, user:<username>, type:[mac|win|lnx], location:<string>
    <servername>:<port>/Delete name:<hostname>

Call Examples:

    curl http://<servername>:<port>/Add -X POST --data name=hostname --data ip=127.0.0.1 --data user=username --data type=[mac|win|lnx] --data location:<string>

    import requests
    resp = requests.get('http://<servername>:<port>/Add', data={'name':'hostname', 'ip':'127.0.0.1', 'user':'username', 'type':'[mac|win|lnx]', 'location':'laptop'})

    docker run -d -p <your port>:80 -v /mnt/machinemap:/data arc2nd/machinemap


