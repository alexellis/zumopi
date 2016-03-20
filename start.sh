#!/bin/sh

systemctl start bluetooth
hciconfig hci0 up

python /home/pi/zumopi/app.py
