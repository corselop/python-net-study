#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from sys import argv
import re

# Обработка файла и красивый вывод информации
# Обработка производится построчно

# Создадим список типов данных для вывода

dataTypes = ['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:']

# Откроем файл, отформатируем и выведем его содержимое

with open('ospf.txt','r') as f:
    for line in f:
        newLine=line.replace(',','').split()
        newLine.remove('via')
        newLine[-1] = newLine[-1]+'\n'
        for i,data in enumerate(dataTypes):
            print "%-30s %-30s" % (dataTypes[int(i)], newLine[int(i)])