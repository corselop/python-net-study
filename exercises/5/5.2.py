#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from sys import argv
import re

# Преобразование MAC-адресов из XXXX:XXXX:XXXX в XXXX.XXXX.XXXX

# список с MAC-адресами

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

# устроим ему валидацию, и если всё хорошо, то приведём к нужному виду

cisco_mac=mac

for i in mac:
    if not re.match(r"^[a-f0-9]{4}\:[a-f0-9]{4}\:[a-f0-9]{4}$",i):
        print 'ввод неверен: ' + i
    else:
        cisco_mac[mac.index(i)]=i.replace(':',".")

print cisco_mac
