#servidor división
#Soto Larios Maribella
import socket
from time import sleep

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=5004
ss.bind((host,port))
print("Server-Division listo")
cont=0
ss.listen(5)
while True:
	cs,addr=ss.accept()
	print("conexion lista con ", str(addr))
	x1=int(cs.recv(1024).decode("ascii"))
	sleep(0.5)
	x2=int(cs.recv(1024).decode("ascii"))
	sleep(0.5)
	cs.send(str(x1/x2).encode("ascii"))
	sleep(0.5)

	cont += 1
	print("Cliente {} atendido".format(cont))
	cs.close()

	if cont == 15:
		print("Ha terminado mi servicio")
		break
ss.close()
input("enter para terminar")