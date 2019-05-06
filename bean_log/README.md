launches a REST service on a uWSGI/NGINX server to write to a specified log file in the mounted volume.  
Logging levels: debug, info, warning, error, critical

Access at: 

    <servername>/Bean app: <log file basename>, level: <logging level>, hostname: <hostname>, ip: <ip address>, user: <username>, msg: <your message text>

Call Examples:

- with curl

        curl http://<servername>:<your port>/Bean -X POST --data app=<log file basename> --data level=<logging level> --data hostname=<hostname> --data ip=<ip address> --data user=<username> --data msg=<your message text>

- with python

        import requests
        url = 'http://<your url>/Bean'
        data_dict = {'app': <log file basename>, 'level': <logging level>, 'hostname': <hostname>, 'ip': <ip address>, 'user': <username>,  'msg': <your message text>}
        resp = requests.post(url, data_dict)

    `docker run -d -p <your port>:80 -v <your data directory>:/data --name <container name> arc2nd/bean_log:latest`



