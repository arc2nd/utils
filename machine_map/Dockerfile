# start with the basics
FROM python:3.6-slim

# copy over our requirements file
COPY requirements.txt /tmp/

# copy over the whole webapp folder
COPY . /srv/webapp
COPY ./mod_map /usr/local/lib/python3.6/site-packages/mod_map
WORKDIR /srv/webapp

# update and install some stuff
RUN apt-get clean && apt-get -y update 
RUN apt-get install -y nginx python3-dev python-pip python-dev build-essential
RUN pip install -r /tmp/requirements.txt

# copy nginx.conf over to our docker nginx install
COPY nginx.conf /etc/nginx/nginx.conf

# setup the start.sh shell script to be runnable
RUN chmod +x ./start.sh
CMD ["./start.sh"]
