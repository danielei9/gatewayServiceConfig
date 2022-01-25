
def getConfig():
    #f = open('test.txt', 'r') #test
    f = open('/etc/dhcpcd.conf', 'r')
    # Si es dinamica
    if( "#static ip_address" in f.read()):
        return "DIN"
    # Si es statica
    else:
        f = open('test.txt', 'r') #test
        for line in f:
            if 'static ip_address' in line:
                ip_adr = line.split('=')[1].split("\n")[0]
                print(ip_adr)
            if 'static routers=' in line:
                gatw = line.split('=')[1].split("\n")[0]
                print(gatw)
        return '{\n   "state": "STAT",\n   "ip_adr": "'+ ip_adr +'",\n   "gatw": "'+ gatw + '"}'
print(getConfig())