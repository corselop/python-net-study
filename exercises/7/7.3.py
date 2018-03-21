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
# создаём словарь, где ключи - интерфейсы, значения - их конфигурация,
# которая пока что пустая
        overall_dict=dict.fromkeys(Ethernets, None)
# запишем конфигурацию порта в значения словаря
        isInterface = False
        interface=''
        ifconfig=[]
        for line in file:
# если нашли строку с Ethernet, то готовимся записывать конфигурацию
# во временный список ifconfig
            if line.find('Ethernet')!=-1:
                isInterface = True
                interface=line.split()[1]
#                print interface
# если натыкаемся на !, то записываем конфигурацию !
# и сбрасываем состояние записи
            elif isInterface and line.startswith('!'):
                isInterface = False
                overall_dict[interface]=ifconfig
                ifconfig=[]
# а здесь сама запись тех строк, что идут до !
            elif isInterface:
                ifconfig.append(line[1:-1])
# теперь можно выбрать access-порты и trunk-порты
# открытый файл нас больше не интересует

    access_list=[]
    trunk_list=[]

#    print overall_dict
# выбираем по наличию ключевого слова access или trunk
# в конфигурации интерфейса
    for key in overall_dict:
#        print overall_dict[key]                        
        if str(overall_dict[key]).find('access')!=-1:
            access_list.append(key)
        if str(overall_dict[key]).find('trunk')!=-1:
            trunk_list.append(key)
#    print access_list
#    print trunk_list
# теперь нужно забрать номера VLAN и засунуть их в итоговые словари
    access_dict=dict.fromkeys(access_list, None)
    trunk_dict=dict.fromkeys(trunk_list, None)
    for interface in access_list:
        access_dict[interface]=re.findall('vlan [0-9]{1,4}',str(overall_dict[interface]))[0].replace('vlan ','')
    for interface in trunk_list:
        trunk_dict[interface]=re.findall('vlan .*?\'',str(overall_dict[interface]))[0][:-1].replace('vlan ','')
    print access_dict
    print trunk_dict

get_int_vlan_map('config_sw1.txt')
