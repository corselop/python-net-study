#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import re

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

#ввод пользовательских данных
device_name = raw_input('Enter device name: ')
device_name = device_name.lower() #case-insensetive
london_co.get(device_name, 'такого девайса нет')
param_name = raw_input('Enter parameter name '+'(' + str(london_co[device_name].keys()).strip('[]') + '): ')
param_name = param_name.lower()
london_co[device_name].get(param_name, 'такого параметра нет')
