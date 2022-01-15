#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
python LYWSD03MMC.py -a -pkt -odl -df sensors.ini -call sendToHABleMonitor.py