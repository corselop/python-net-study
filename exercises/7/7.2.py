#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# фукнция, которая генерирует конфигурацию для trunk-портов

# эта функция получает на вход словарь и возвращает словарь
# с ключами типа FastEthernet0/1

# это словарь
trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }


# функция
def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    config_dict=dict.fromkeys(trunk_dict.keys(), None)

    for interface in trunk_dict:
#        config.append('interface ' + interface)
#        print access[interface]
        config_local=[]
        for item in trunk_template:
            if re.search('allowed',item):
                config_local.append(item + ' ' + ' '.join(str(i) for i in trunk_dict[interface]))
            else:
                config_local.append(item)
#        if psecurity:
#            for item in port_security:
#                config_local.append(item)
        config_dict[interface]=config_local

    print config_dict

generate_trunk_config(trunk_dict)
