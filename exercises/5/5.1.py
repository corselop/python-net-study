#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from sys import argv
import re

# Проверка корректности адреса и определение его класса

# Инициируем pass_OK - если не True, запрашиваем ввод ещё раз

pass_OK = False

while not pass_OK:
    ip_initial = raw_input('Введите IPv4 адрес в формате x.x.x.x: ')
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_initial):
        print 'ввод неверен'
    else:
        octets = ip_initial.split('.')
        for i in range (4):
            octets[i] = int(octets[i])
        print octets
        if not 0 <= octets[0] <= 255:
            print 'Incorrect IPv4 address'
            ip_initial = raw_input('Введите IPv4 адрес в формате x.x.x.x: ')
        elif not 0 <= octets[1] <= 255:
            print 'Incorrect IPv4 address'
            ip_initial = raw_input('Введите IPv4 адрес в формате x.x.x.x: ')
        elif not 0 <= octets[2] <= 255:
            print 'Incorrect IPv4 address'
            ip_initial = raw_input('Введите IPv4 адрес в формате x.x.x.x: ')
        elif not 0 <= octets[3] <= 255:
            print 'Incorrect IPv4 address'
            ip_initial = raw_input('Введите IPv4 адрес в формате x.x.x.x: ')
        else:
            pass_OK = True

address_type='unused' #делаем тип по умолчанию

if ip_initial == '255.255.255.255':
    address_type='local broadcast'
elif ip_initial == '0.0.0.0':
    address_type='unassigned'
elif 1 <= octets[0] <= 127:
    address_type='unicast (Class A)'
elif 128 <= octets[0] <= 191:
    address_type='unicast (Class B)'
elif 192 <= octets[0] <= 223:
    address_type='unicast (Class C)'
elif 224 <= octets[0] <= 239:
    address_type='multicast'

print address_type