#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from sys import argv
import re

# Генератор конфигурации для access и trunk портов

# шаблоны для типов портов

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

# кое-какие данные

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'}, 
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

# генератор для access-портов

for int in fast_int['access']:
    print 'interface FastEthernet' + int
    for command in access_template:
        if command.endswith('access vlan'):
            print ' %s %s' % (command, fast_int['access'][int])
        else:
            print ' %s' % command

# генератор для транк-портов

for int in fast_int['trunk']:
    print 'interfade FastEthernet' + int
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if fast_int['trunk'][int][0]=='only':
                print ' %s %s' % (command, str(fast_int['trunk'][int][1:]).translate(None,'[]\''))
            elif fast_int['trunk'][int][0]=='add':
                print ' %s %s %s' % (command, 'add', str(fast_int['trunk'][int][1:]).translate(None,'[]\''))
            elif fast_int['trunk'][int][0]=='del':
                print ' %s %s %s' % (command, 'del', str(fast_int['trunk'][int][1:]).translate(None,'[]\''))
        else:
            print ' %s' % command
