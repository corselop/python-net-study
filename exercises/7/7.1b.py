#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# фукнция, которая генерирует конфигурацию для access-портов

# эта функция получает на вход словарь и возвращает словарь
# с ключами типа FastEthernet0/1

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

    config_dict=dict.fromkeys(access.keys(), None)

    for interface in access:
#        config.append('interface ' + interface)
#        print access[interface]
        config_local=[]
        for item in access_template:
            if re.search('vlan',item):
                config_local.append(item + '' + str(access[interface]))
            else:
                config_local.append(item)
        if psecurity:
            for item in port_security:
                config_local.append(item)
        config_dict[interface]=config_local

    print config_dict

generate_access_config(access_dict,psecurity=True)