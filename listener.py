# Ce programme doit être lancé avec les permissions 'root'
import socket

ip = "206.167.46.204"
port = 420

# Création de l'objet 'socket'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connexion au port local
s.bind((ip,port))

fd = open("/etc/Watchmen/Watchmen_serveur.conf", 'r')
position = fd.read()
position2=position.split('\n')
fd.close()

# Boucle d'écoute
while True:
# Réception des données et affichage
	donnees,addr = s.recvfrom(1024)
	print("Message UDP de", addr, ": ", donnees)

	f=open(position2[0],'r')
	file=f.read()
	file=(file + ("Message UDP de" + str(addr) + ":" + str(donnees) + '\n'))
	f.close()

	f=open(position2[0],'w')
	f.write(file)
	f.close()

s.close()
print('Termine.')
