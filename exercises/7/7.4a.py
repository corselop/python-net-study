#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# функция, которая читает файл с конфигурацией коммутатора
# и составляет словари согласно степени вложенности:
# самый вложенный уровень должен быть списком, остальные - словарями

# функция
def get_config_dict(filename):
    """
    возвращает словарь, где список - набор команд нижнего уровня, 
    а словари - команды верхних; ориентирована на то, что уровней
    вложенности максимум 3

    """

# создаём словарь для всей конфигурации
    overall_dict={}
# открываем файл на чтение
    with open(filename,'r') as file:
# инициализируем переменные для цикла,
# указывающие на уровень вложенности
        level1 = False
        level2 = False
        topCommand = ''
        l1Command = ''
        l2Command = ''
        config1 = []
        config2 = []
        for line in file:
# игнорируем пустые строки
            if not line.strip:
                continue
# игнорируем строки с ! вне контекста
            elif line.startswith('!') and (not level1 or not level2):
                continue
# если встретили ! следом за командами, сбрасываем индикаторы 
            elif line.startswith('!') and level1:
                level1 = False
                level2 = False
# если встретили пробел в начале строки - обрабатываем по индикаторам
# если встретили ситуацию ниже - это ошибка файла конфигурации, сбрасываем индикаторы
            elif line.startswith(' ') and not level1 and not level2:
                level1 = False
                level2 = False
# если встретили пробел и есть указание на начало первого вложения
            elif line.startswith(' ') and level1 and not level2:
                l1Command = line.strip()
                config1.append(l1Command)
# а это возврат со второго уровня на первый
            elif line.startswith(' ') and level1 and level2:
                
            elif line.startswith('  ') and level2:
            elif line.startswith('  ') and not level2:
            else:
                level1 = True
                topCommand = line.strip()
                overall_dict[topCommand]=[]

# список всех команд верхнего уровня
#    keyList=[]
# открываем файл
#    with open(filename,'r') as file:
#        for line in file:
# игнорируем пустые строки
#            if not line.strip:
#                continue
# ищем строки с командами верхнего уровня Ethernet
#            elif line.startswith(' '):
#                pass
#            elif line.startswith('!'):
#                pass
#            else:
#                keyList.append(line.strip())
#        keyList.remove('')
# перемещаемся в начало файла
#        file.seek(0)
#        print keyList
# создаём словарь, где ключи - команды верхнего уровня, значения - их подкоманды,
# которые пока что пустые
#        overall_dict=dict.fromkeys(keyList, None)
# запишем подкоманды словаря
#        isCommand = False
#        command=''
#        config=[]
#        for line in file:
# игнорируем пустые строки
#            if not line.strip():
#                continue
# если нашли строку с командой, то готовимся записывать конфигурацию
# во временный список config
#            if (line.startswith(' ')==False) or (line.startswith('!')==False):
#            elif line.startswith('!') and not isCommand:
#                print 1
#                pass
#            elif line.startswith('!') and isCommand:
#                isCommand = False
#                overall_dict[command]=config
#                config=[]
#                print overall_dict[command]
#            elif line.startswith(' ') and isCommand:
#                config.append(line.strip())
#            elif line.startswith(' ') and not isCommand:
#                pass
#            else:
#                isCommand = True
#                command = line.strip()
#                overall_dict[command]=[]
# открытый файл нас больше не интересует

    print overall_dict

get_config_dict('config_sw1.txt')
