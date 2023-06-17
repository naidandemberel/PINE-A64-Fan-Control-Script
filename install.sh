#!/bin/bash

if [ $(id -u) -ne 0 ]
    then
     	echo Please run as root
	exit 1
fi

echo Copying files 

cp fan_control.py /usr/local/bin
cp fan_control.service /etc/systemd/system

echo Starting fan_control.service

systemctl daemon-reload
sleep 1 

systemctl enable fan_control.service
sleep 1

systemctl start fan_control.service
sleep 1
