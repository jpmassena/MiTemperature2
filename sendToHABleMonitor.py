#!/usr/bin/python

from requests import post
import sys

# fields,sensorname,temperature,humidity,voltage,timestamp,packet
payload = {"packet": sys.argv[7]}

url = "http://ha_ip:8123/api/services/ble_monitor/parse_data"
headers = {
    "Authorization": "Bearer long_lived_token_from_home_assistant",
    "content-type": "application/json",
}

post(url, headers=headers, json=payload)
