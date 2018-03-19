#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# функция, которая читает файл с конфигурацией коммутатора
# и составляет словари портов в режиме access и trunk,
# где значение - это списки VLAN

# функция
def get_int_vlan_map(filename):
    """
    возвращает два словаря, где ключ - порт, значение - список VLAN

    trunk - словарь trunk-портов.

    access - словарь access-портов.

    """

# список всех интерфейсов
    Ethernets=[]
# открываем файл
    with open(filename,'r') as file:
        for line in file:
# ищем строки с интерфейсами и записываем интерфейсы в Ethernet
            if re.search('Ethernet',line):
                Ethernets.append(line.split()[1])
# перемещаемся в начало файла
        file.seek(0)
# создаём словарь, где ключи - интерфейсы, значения - их конфигурация
        overall_dict=dict.fromkeys(Ethernets, None)
# запишем конфигурацию порта в значения
        isInterface = False
        interface=''
        ifconfig=[]
        for line in file:
            if re.search('Ethernet',line):
                isInterface = True
                interface=line.split()[1]
                print interface
            elif isInterface and line.startswith('!'):
                isInterface = False
                overall_dict[interface]=ifconfig
                ifconfig=[]
            elif isInterface:
                ifconfig.append(line[1:-1])
# теперь нужно выбрать access-порты и trunk-порты
# открытый файл нас больше не интересует

    for key in overall_dict:
        print overall_dict[key]                        
                
#    print overall_dict
    
#    config_dict=dict.fromkeys(trunk_dict.keys(), None)

#    for interface in trunk_dict:
#        config.append('interface ' + interface)
#        print access[interface]
#        config_local=[]
#        for item in trunk_template:
#            if re.search('allowed',item):
#                config_local.append(item + ' ' + ' '.join(str(i) for i in trunk_dict[interface]))
#            else:
#                config_local.append(item)
#        if psecurity:
#            for item in port_security:
#                config_local.append(item)
#        config_dict[interface]=config_local

#    print config_dict

get_int_vlan_map('config_sw1.txt')
