#!/bin/bash

sudo docker run \
-itd \
-p 1883:1883 \
-p 9001:9001 \
-v /mnt/mosquitto/conf/mosquitto.conf:/mosquitto/config/mosquitto.conf:ro \
-v /mnt/mosquitto/data:/mosquitto/data \
-v /mnt/mosquitto/log:/mosquitto/log \
eclipse-mosquitto

