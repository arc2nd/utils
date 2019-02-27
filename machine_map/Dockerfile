# start with ubuntu
FROM ubuntu:latest

# copy over our requirements file
COPY requirements.txt /tmp/

# update and install some stuff
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r /tmp/requirements.txt

# copy over the app directory
COPY ./app /app

# set working directory and run the app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]

