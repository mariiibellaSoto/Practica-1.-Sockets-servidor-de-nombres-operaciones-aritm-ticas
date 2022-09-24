#servidor nombres
#Soto Larios Maribella
#Torres Amezcua Maria Guadalupe
import socket
from time import sleep

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=5000
ss.bind((host,port))
print("Server-Nombres listo")
cont=0
ss.listen(5)

while True:
	cs,addr=ss.accept()
	print("conexion lista con ", str(addr))
	cont += 1
	respuesta = cs.recv(1024)
	sleep(0.5)
	respuesta = respuesta.decode("ascii")
	#Proporcionar datos para la comunicación con el Servidor Suma
	if respuesta == "1":
		ipenviada = host
		portenviado = 5001
	#Proporcionar datos para la comunicación con el Servidor Resta
	elif respuesta == "2":
		ipenviada = host
		portenviado = 5002
	#Proporcionar datos para la comunicación con el Servidor Multiplicacion
	elif respuesta == "3":
		ipenviada = host
		portenviado = 5003
	#Proporcionar datos para la comunicación con el Servidor Division
	elif respuesta == "4":
		ipenviada = host
		portenviado = 5004
	#Proporcionar datos para la comunicación con el Servidor Módulo
	elif respuesta == "5":
		ipenviada = host
		portenviado = 5005
	#Proporcionar datos para la comunicación con el Servidor Potencia
	elif respuesta == "6":
		ipenviada = host
		portenviado = 5006
	else:
		pass

	if respuesta == "X" or respuesta == "x":
		pass
	else:
		cs.send(ipenviada.encode("ascii"))
		sleep(0.5)
		cs.send(str(portenviado).encode("ascii"))
		sleep(0.5)

	print("Cliente {} atendido".format(cont))
	cs.close()

	if cont == 15:
		print("Ha terminado mi servicio")
		break
ss.close()
input("enter para terminar")
