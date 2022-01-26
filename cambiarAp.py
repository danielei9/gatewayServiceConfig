#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulo python Daniel Burruchaga Sola

import sys
import os
import time

def changeSSID(ssid):
    #'/usr/local/rak/ap/Create_ap.conf'
    ssid_last = ""
    txtFile = []
    if(ssid != None):
        #file = open("test_ap.txt", 'r')
        file = open("/usr/local/rak/ap/Create_ap.conf", 'r')
        lines = file.readlines()
        #print(lines)
        for l in lines:
            if("SSID" in l):
                ssid_last = l.split('=')[1]
                lineSSID = l.replace(ssid_last,str(ssid)+"\n")   
                print(lineSSID)
                txtFile.append(lineSSID)
            else:
                txtFile.append(l)
        file.close()       
        file = open("/usr/local/rak/ap/Create_ap.conf", 'w')
        file.writelines(txtFile)
        file.close()

def changePSWD(pswd):
    pswd_last = ""
    txtFile = []
    if(pswd != None):
    #'/usr/local/rak/ap/Create_ap.conf'
        #file = open("test_ap.txt", 'r')
        file = open("/usr/local/rak/ap/Create_ap.conf", 'r')
        lines = file.readlines()
        #print(lines)
        for l in lines:
            if("PASSPHRASE" in l):
                pswd_last = l.split('=')[1]
                linePSWD = l.replace(pswd_last, str(pswd)+"\n")   
                print(linePSWD)
                txtFile.append(linePSWD)
            else:
                txtFile.append(l)
        file.close()       
        file = open("/usr/local/rak/ap/Create_ap.conf", 'w')
        file.writelines(txtFile)
        file.close()

def changeAp(ssid, pswd):
    print(ssid)
    changeSSID(ssid)
    changePSWD(pswd)
    os.system('sudo reboot')
