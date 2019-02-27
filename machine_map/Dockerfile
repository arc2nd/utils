FROM ubuntu:latest

COPY requirements.txt /tmp/

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]

