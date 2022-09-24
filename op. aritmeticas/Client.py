#cliente
#Soto Larios Maribella
import socket
from time import sleep

def accion(opc):
	ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host=socket.gethostname()
	port=5000
	ss.connect((host,port))

	print("Inicia la comunicación con el servidor Nombres")
	print("IP: {}".format(host))
	print("Puerto: {}\n".format(port))
	ss.send(opc.encode("ascii"))
	ip=ss.recv(1024)
	sleep(0.5)
	puerto = ss.recv(1024)
	sleep(0.5)
	ip=ip.decode("ascii")
	puerto= int(puerto.decode("ascii"))
	print("Datos del Servidor requerido\nIP= {}\nPort= {}\n\n".format(ip,puerto))
	ss.close()
	valido = False
	while valido == False:
		x1 = input("Ingresa el primer valor=> ")
		x2 = input("Ingresa el segundo valor=> ")
		try:
			x1 = int(x1)
			x2 = int(x2)
			if opc == "4" or opc == "5" or opc == "6":
				if x2 < 1 and x2 >= 0:
					print ("El segundo valor no puede ser 0!!!!")
				else:
					valido = True
			else:
				valido = True
				break
		except:
			print("Ingresa solamente numeros enteros!!!!!")

	print("Vamos a conectarnos con el servidor que hará la operacion...")
	sleep(0.5)
	s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1.connect((ip,int(puerto)))
	print("¡Lo tenemos!\n")
	s1.send(str(x1).encode("ascii"))
	sleep(0.5)
	s1.send(str(x2).encode("ascii"))
	sleep(0.5)
	resultado = s1.recv(1024)
	resultado = resultado.decode("ascii")
	s1.close

	if opc == "1":
		print("Resultado:\n{} + {} = {}".format(x1,x2,resultado))
	elif opc == "2":
		print("Resultado:\n{} - {} = {}".format(x1,x2,resultado))
	elif opc == "3":
		print("Resultado:\n{} * {} = {}".format(x1,x2,resultado))
	elif opc == "4":
		print("Resultado:\n{} / {} = {}".format(x1,x2,resultado))
	elif opc == "5":
		print("Resultado:\n{} % {} = {}".format(x1,x2,resultado))
	else:
		print("Resultado:\n{} ^ {} = {}".format(x1,x2,resultado))

def main():
	termina = False

	while termina == False:
		print("\n\n---------Operaciones aritmeticas---------");
		opcCorrecta=False
		while opcCorrecta==False:
			print("[1]Suma\n[2]Resta\n[3]Multiplicación\n[4]División\n[5]Módulo\n[6]Potencia\n[x]Salir")
			opcion = input("¿Que operacion deseas hacer?=> ")

			if opcion == "1":
				print("\nServidor Nombres nos dará los datos del Servidor Suma para luego comunicarnos con el")
				accion(opcion)
				opcCorrecta=True
			elif opcion == "2":
				print("\nServidor Nombres nos dará los datos del Servidor Resta para luego comunicarnos con el")
				accion(opcion)
				opcCorrecta=True
			elif opcion == "3":
				print("\nServidor Nombres nos dará los datos del Servidor Multiplicacion para luego comunicarnos con el")
				accion(opcion)
				opcCorrecta=True
			elif opcion == "4":
				print("\nServidor Nombres nos dará los datos del Servidor Division para luego comunicarnos con el")
				accion(opcion)
				opcCorrecta=True
			elif opcion == "5":
				print("\nServidor Nombres nos dará los datos del Servidor Modulo para luego comunicarnos con el")
				accion(opcion)
				opcCorrecta=True
			elif opcion == "6":
				print("\nServidor Nombres nos dará los datos del Servidor Potencia para luego comunicarnos con el")
				accion(opcion)
				opcCorrecta=True
			elif opcion == "x" or opcion == "X":
				print("Saliendo...")
				termina = True
				#ss.send(opcion.encode("ascii"))
				break
			else:
				print("Dame una respuesta valida, por favor")

if __name__ == '__main__':
	main()
