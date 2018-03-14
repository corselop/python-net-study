#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter
import re

# Очистка таблицы с MAC-адресами от ненужного и потом поиск по VLAN
# Обработка производится построчно

# имена файлов указывать не нужно, нужно указать номера VLAN

# запросим VLAN

# Запросим имена файлов
vlans = argv[1:]
# Проверка, что на входе что-то есть
if not vlans:
    print 'не выбрано ни одного VLANа'
    quit()
# а теперь проверим, что поданы vlanid 
for i in vlans:
    if not re.match(r"^[0-9]{1,4}",i):
        print 'ввод неверен: ' + i
        quit()
    elif not 1 <= int(i) <= 4096:
        print 'ввод неверен: ' + i
        quit()

# открываем файл на чтение и нчинаем манипуляции
# идея такая: сделать список списков с содержимым строк

try:
    with open ('CAM_table.txt','r') as f:
        i = 0
        l = 0
        for line in f:
            if re.search(r"([0-9a-fA-F].?){12}",line):
                i += 1
#это было для определения размера списка для строк
        strings = ['' for k in range(i)]
        f.seek(0)
#начинаем заново и забираем строки с MAC-адресами в список
        for line in f:
            if re.search(r"([0-9a-fA-F].?){12}",line):
                strings[l]=line
                l += 1
#пробуем из списка сделать словарь
    d = [k for k in range(i)]
    for k in range(i):
        strings[k] = strings[k].split()
#    dictionary = dict(zip(d,strings))
#сделали, теперь можем сортировать
    strings_sorted = sorted(strings, key=itemgetter(0))
#и теперь сделаем вывод только нужных нам VLAN, которые указали на входе
    for i in vlans:
        for string in strings_sorted:
            if re.match(i,string[0]):
                print "%-15s %-15s %-15s" % (string[0],string[1],string[3])   
    
except IOError:
    print ' \n'
    print 'no such file: CAM_table.txt'


