#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from sys import argv
import re

# Проверка корректности адреса и определение его класса

# Инициируем

ip_initial = raw_input('Введите IPv4 адрес в формате x.x.x.x: ')
#верификация регулярным выражением как первый этап - что подсунули хотя бы по виду
#подходящее.
if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_initial):
    print 'ввод неверен'
    quit()

#готовим данные в к более подробной проверке, а также к другим манипуляциям
octets = ip_initial.split('.')

#print octets

#приступим к проверкам

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