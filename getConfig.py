
def getSSID():
    #'/usr/local/rak/ap/Create_ap.conf'
    ssid_last = ""
    file = open("/usr/local/rak/ap/create_ap.conf", 'r')
    lines = file.readlines()
    for l in lines:
        if("SSID" in l):
            print(l)
            print("l")
            ssid_last = l.split('=')[1].split('\n')[0]
            return ssid_last
        else:
            ssid_last = ""
    file.close()
    print(ssid_last)
    return ssid_last

def getPSWD():
    #'/usr/local/rak/ap/Create_ap.conf'
    pswd_last = ""
    file = open("/usr/local/rak/ap/create_ap.conf", 'r')
    lines = file.readlines()
    for l in lines:
        if("PASSPHRASE" in l):
            pswd_last = l.split('=')[1].split('\n')[0]
            return pswd_last
        else:
            pswd_last = ""
    file.close()
    print(pswd_last)
    return pswd_last       

def getConfig():
    f = open('test.txt', 'r') #test
    ssid = getSSID()
    pswd = getPSWD()
    #f = open('/etc/dhcpcd.conf', 'r')
    # Si es dinamica
    if("#static ip_address" in f.read()):
        return '{\n   "state": "DIN",\n   "ssid": "'+str(ssid)+'",\n   "pswd": "'+str(pswd)+'"\n}'
    # Si es statica
    else:
        # f = open('test.txt', 'r')  # test
        f = open('/etc/dhcpcd.conf', 'r')
        for line in f:
            if 'static ip_address' in line:
                ip_adr = line.split('=')[1].split("\n")[0]
                print(ip_adr)
            if 'static routers=' in line:
                gatw = line.split('=')[1].split("\n")[0]
                print(gatw)
    
    return '{\n   "state": "STAT",\n   "ip_adr": "' + ip_adr +'",\n   "gatw": "'+ gatw + '",\n   "ssid": "'+str(ssid)+'",\n   "pswd": "'+str(pswd)+'"\n}'

print(getConfig())