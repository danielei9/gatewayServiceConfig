
crontab -e :

@reboot sudo ./home/pi/gatewayServiceConfig/init-python.sh  > /tmp/port_7777.log 2>&1
@reboot cd /home/pi/gatewayServiceConfig && /usr/bin/python3 init-server.py > /tmp/server_7777.log 2>&1

dar permisos de ejecucion 
chmod +x /home/pi/gatewayServiceConfig/init-python.sh
chmod +x /home/pi/gatewayServiceConfig/init-server.py 
REVISAR LOS ARCHVOS DE CONFIG AP Y DHCP SI DA ERRORES HABRA QUE BORRAR ALGUNA LINEA COMENTADA REPETIDA