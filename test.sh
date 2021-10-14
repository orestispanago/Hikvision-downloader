#!/bin/bash

USER="YourUsername"
PASS="YourPassword"
IP="150.140.194.27"

BASE_URL="http://${USER}:${PASS}@${IP}"

DATE_TIME=$(date -u "+%y%m%d_%H%M%S") # UTC

THERMAL_PIC_URL="${BASE_URL}/ISAPI/Streaming/channels/2/picture"
VISIBLE_PIC_URL="${BASE_URL}/ISAPI/Streaming/channels/1/picture"
JSON_URL="${BASE_URL}/ISAPI/Thermal/channels/2/thermometry/1/rulesTemperatureInfo?format=json"

wget $THERMAL_PIC_URL -O "${DATE_TIME}_t.jpeg"
wget $VISIBLE_PIC_URL -O "${DATE_TIME}_v.jpeg"
wget $JSON_URL -O "${DATE_TIME}.json"

# timed 0.738s from home wifi