#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# функция, которая читает файл с конфигурацией коммутатора
# и составляет словари, где ключ - команда верхнего уровня,
#  значение - это подкоманды

# функция
def get_int_vlan_map(filename):
    """
    возвращает словарь, где ключ - команда верхнего уровня, 
    значение - подкоманды

    """

# список всех команд верхнего уровня
    keyList=[]
# открываем файл
    with open(filename,'r') as file:
        for line in file:
# игнорируем пустые строки
            if not line.strip:
                continue
# ищем строки с командами верхнего уровня Ethernet
            elif line.startswith(' '):
                pass
            elif line.startswith('!'):
                pass
            else:
                keyList.append(line.strip())
        keyList.remove('')
# перемещаемся в начало файла
        file.seek(0)
#        print keyList
# создаём словарь, где ключи - команды верхнего уровня, значения - их подкоманды,
# которые пока что пустые
        overall_dict=dict.fromkeys(keyList, None)
# запишем подкоманды словаря
        isCommand = False
        command=''
        config=[]
        for line in file:
# игнорируем пустые строки
            if not line.strip():
                continue
# если нашли строку с командой, то готовимся записывать конфигурацию
# во временный список config
#            if (line.startswith(' ')==False) or (line.startswith('!')==False):
            elif line.startswith('!') and not isCommand:
#                print 1
                pass
            elif line.startswith('!') and isCommand:
                isCommand = False
                overall_dict[command]=config
                config=[]
#                print overall_dict[command]
            elif line.startswith(' ') and isCommand:
                config.append(line.strip())
            elif line.startswith(' ') and not isCommand:
                pass
            else:
                isCommand = True
                command = line.strip()
                overall_dict[command]=[]
# открытый файл нас больше не интересует

    print overall_dict

get_int_vlan_map('config_sw1.txt')
