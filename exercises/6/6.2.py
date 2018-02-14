#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import re

# Обработка файла на вводе скрипта с удалением ненужных строк
# Обработка производится построчно

# Запросим имена файлов
fileNames = argv[1:]
# Проверка, что на входе что-то есть
if not fileNames:
    print 'не выбрано ни одного файла'
    quit()
# а что файл существует, проверим в цикле вывода
# зададим слова-исключения, строки с которыми не выводятся
ignore = ['duplex','alias','Current configuration']

# основной цикл с проверками
for i,file in enumerate(fileNames):
    try:
        with open(fileNames[i],'r') as f:
            for line in f:
# зададим переменную, обозначающую успешность проверок
                ignoreLine=False
                if line[0]=='!':
                    ignoreLine=True
# проверили, что начало там не !
                if ignoreLine==False:
                    for word in ignore:
                        if re.search(word,line):
                            ignoreLine=True
                
                if ignoreLine==False:
                    print line[:-1]

    except IOError:
        print ' \n'
        print 'no such file: '+fileNames[i]