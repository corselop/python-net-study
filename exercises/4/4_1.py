#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import re

#ввод пользовательских данных
ip_initial = raw_input('Введите IP-сеть в формате x.x.x.x/yy: ')


#верификация регулярным выражением проверка далеко не идеальная, но на данном этапе нормальная
if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$",ip_initial):
    print 'ввод неверен'
    quit()

#ниже - огромное выражение на валидный IPv4 адрес ValidIpAddressRegex =
#"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\/\d{1,2}$
"
print 'ввод верен!'

#идём дальше
derived = ip_initial.split('/')

network_decimal = derived[0].split('.')
mask_decimal = derived[1]

#получили значения по отдельности
#print network_decimal, mask_decimal

#готовим лист
network_bin_list = ['' for i in range (4)]

#переводим десятичные записи в двоичные и добавляем в лист
for i in range (4):
    network_bin_list[i] = format(int(network_decimal[i]), '08b')

#формируем маску сети
mask_bin = '1'*int(mask_decimal)+'0'*(32-int(mask_decimal))

#разбиваем маску на октеты
chunks, chunk_size = len(mask_bin), len(mask_bin)/4
mask_bin_list = [mask_bin[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

#print mask_bin_list

#не забываем про десятичную маску
mask_dec_list = ['' for i in range (4)]
for i in range (4):
    mask_dec_list[i] = int(mask_bin_list[i],2)

#всё готово к финальному выводу
print 'Network:'
print '%-15s %-15s %-15s %-15s' % (network_decimal[0], network_decimal[1], network_decimal[2], network_decimal[3])
print '%-15s %-15s %-15s %-15s' % (network_bin_list[0], network_bin_list[1], network_bin_list[2], network_bin_list[3
])

print 'Mask:'
print '/'+mask_decimal
print '%-15s %-15s %-15s %-15s' % (mask_dec_list[0], mask_dec_list[1], mask_dec_list[2], mask_dec_list[3])
print '%-15s %-15s %-15s %-15s' % (mask_bin_list[0], mask_bin_list[2], mask_bin_list[2], mask_bin_list[3])