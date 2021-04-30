import socket
import time
from datetime import datetime
from gpiozero import Button

etat = 1
Porte_1 = Button(6)
Porte_2 = Button(13)
Porte_3 = Button(19)
Fenetre = Button(26)
Valeur_Cap = " "

f = open("/etc/Watchmen/Watchmen_collecteur.conf")
sip = f.read()

ip_tampo = sip.split('\n')
ip = ip_tampo[0]
f.close()

print(ip)

port = 420

# Cr  ation de l'objet 'socket'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(etat):
	#lecture des capteur
	if Porte_1.is_pressed:
		Valeur_Cap = "1"
	else:
		Valeur_Cap = "0"
	if Porte_2.is_pressed:
		Valeur_Cap = Valeur_Cap + "1"
	else:
		Valeur_Cap = Valeur_Cap + "0"
	if Porte_3.is_pressed:
		Valeur_Cap = Valeur_Cap + "1"
	else:
		Valeur_Cap = Valeur_Cap + "0"
	if Fenetre.is_pressed:
		Valeur_Cap = Valeur_Cap + "1"
	else:
		Valeur_Cap = Valeur_Cap + "0"
	#lecture donne capteur memoire
	fCap = open("/home/pi/projet_prog/donner_capteur.log", 'r')
	file_Cap = fCap.read()
	donne_Cap = file_Cap.split('\n')
	fCap.close()
	#traitement donne
	if donne_Cap[0] != Valeur_Cap:
		fCap = open("/home/pi/projet_prog/donner_capteur.log",'w')
		fCap.write(Valeur_Cap)
		fCap.close()
		#set date de lecture
		d = datetime.now()
		i = d.strftime("%Y-%m-%d")
		#envoie du message
		msgs = bytes(Valeur_Cap + "." + i, 'ascii')
		envoye = s.sendto(msgs,(ip,port))
		print(Valeur_Cap)
s.close()
print('Termin  .')

