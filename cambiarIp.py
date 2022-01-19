#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modulo python Daniel Burruchaga Sola 

import sys
import os
import requests
import time

f = open('test.txt', 'w')
f.write ("Número de parámetros: " +  str(len(sys.argv)))
f.write ("Lista de argumentos: " + str(sys.argv))
#sudo nano /etc/dhcpcd.conf 

f.write("hola mundo")
f.close()




 