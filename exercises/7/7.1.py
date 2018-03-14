#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# фукнция, которая генерирует конфигурацию для access-портов

# эта функция получает на вход словарь и возвращает конфигурацию на основе шаблона

# это словарь
access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

# функция

def generate_access_config(access,psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    config=[]

    for interface in access:
        config.append('interface ' + interface)
#        print access[interface]
        for item in access_template:
            if re.search('vlan',item):
                config.append(item + '' + str(access[interface]))
            else:
                config.append(item)
        if psecurity:
            for item in port_security:
                config.append(item)

    print config

generate_access_config(access_dict,psecurity=True)