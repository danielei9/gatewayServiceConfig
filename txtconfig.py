#-----dejamos el gateway con dhcp
#sudo nano /etc/dhcpcd.conf
#Añadiremos al final del archivo (movernos con cursor) y añadiremos lo siguiente:
ipDHCP = """
# WARNING:Do not delete or modify the following 5 lines!!!
# RAK_eth0_IP
interface eth0
#static ip_address=192.168.1.22
#static routers=192.168.1.1
#static domain_name_servers=192.168.1.1 8.8.8.8
static domain_name_servers=8.8.8.8"""

#PARA PONER IP FIJA 22
# Para resolver esto iremos a: sudo nano /etc/dhcpcd.conf
#Añadiremos al final del archivo (movernos con cursor) y añadiremos lo siguiente:

ipFija = """# WARNING:Do not delete or modify the following 5 lines!!!
# RAK_eth0_IP
interface eth0
static ip_address=192.168.1.22
static routers=192.168.1.1
static domain_name_servers=192.168.1.1 8.8.8.8"""