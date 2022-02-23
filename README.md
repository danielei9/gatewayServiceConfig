

Si ya esta instalado el arduino nano y los leds saltar este paso:

// Dependencies Actualización
sudo apt-get upgrade
sudo apt-get update

Instalacion de pip: Sabremos si esta instalado mediante el comando en terminal de: 
sudo apt install python3-pip -y pip3 --version

Despues ejecutamos:
- pip3 install pyserial
- pip3 install paho-mqtt python-etcd 
- pip3 install psutil
- pip3 install flask

// PARAMETROS DE INSTALACION DEL SERVICIO //
Hacer git clone de este repositorio en /home/pi/
Entrar en crontab -e mediante una terminal, y escribir dentro del archivo (sin comillas): 

"
@reboot sudo /home/pi/gatewayServiceConfig/init-python.sh > /tmp/port_7777.log 2>&1
"

dar permisos de ejecucion mediante terminal con: 
chmod +x /home/pi/gatewayServiceConfig/init-python.sh
chmod +x /home/pi/gatewayServiceConfig/init-server.py 

podemos ver el log al reinicar --> nano /tmp/server_7777.log /home/pi/gateway-Service/init-python.sh --> python3 /home/pi/gateway-Service/Reset\ Service.py

REVISAR LOS ARCHVOS DE CONFIG AP Y DHCP SI DA ERRORES HABRA QUE BORRAR ALGUNA LINEA COMENTADA REPETIDA

probar si todo va bien cd gatewayServiceConfig ./init-python.sh
se puede probar despues de correr este programa y con el corriendo realizar un curl al localhost:7777 con el comando curl localhos:7777
o haciendo reboot y luego curl localhost:7777

Apuntes : resumen
--------------------------------
Actualizar e instalar pip3 
instalar flask
crontab -e :
@reboot sudo /home/pi/gatewayServiceConfig/init-python.sh > /tmp/port_7777.log 2>&1
dar permisos de ejecucion 
chmod +x /home/pi/gatewayServiceConfig/init-python.sh
chmod +x /home/pi/gatewayServiceConfig/init-server.py 
REVISAR LOS ARCHVOS DE CONFIG AP Y DHCP SI DA ERRORES HABRA QUE BORRAR ALGUNA LINEA COMENTADA REPETIDA
