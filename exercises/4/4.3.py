#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import re

access_template = ['switchport mode access',
                   'switchport access vlan %s',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan %s']

#setting interface modes for input check
modes = ['access', 'trunk']

#setting phrases for different modes
phrases = ['Enter VLAN number: ','Enter allowed VLANs: ']

#defining strings for different modes
vlans_dict = dict(zip(modes,phrases))

#user input
inf_mode = raw_input('Enter interface mode (access/trunk): ')
inf_mode = inf_mode.lower() # make case-insensetive
inf_mode in modes # user input checking

eth = raw_input('Enter interface type and number: ')

vlans = raw_input('' + vlans_dict[inf_mode])

#making lists for output
output = dict(zip(modes,[access_template,trunk_template]))

#output
print 'interface %s' % eth
for i in range(len(output[inf_mode])):
    print output[inf_mode][i] % vlans