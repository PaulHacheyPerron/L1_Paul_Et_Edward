from flask import Flask,request,render_template
from datetime import datetime

Watchmen = Flask(__name__)

@Watchmen.route('/')
@Watchmen.route('/index')
def index(elem):
	fb = open("/home/tge/Watchmen/donne.log")
	position1 = fb.read()
	fb.close()

	return elem[1] 
        #return render_template("patron.html")

@Watchmen.route('/fheure')
def Historique():
	return render_template("patron-fheure.html")

@Watchmen.route('/rheure')
def R_Heure():
	Nb_Heure = request.args.get('heure')
	Porte_1 = 0
	Porte_2 = 0
	Porte_3 = 0
	Porte_4 = 0
	if Nb_Heure.isdigit():
		Nb_Heure = Nb_Heure
	else:
		Nb_Heure = 0

	f = open("/home/tge/Watchmen/donne.log")
	file = f.readlines()
	f.close()
	last_line = file[len(file)-1]
	ref_date = last_line.split("<br/>")
	ref_date = ref_date[0].split('.')
	ref_date = ref_date[1].split('-')

	Min_date = int(ref_date[3]) - int(Nb_Heure)
	data_actif = " "

	if Min_date < 0:
		Min_date = 0
	elif Min_date > 24:
		Min_date = 24
	#prendre les lignes dans les heure aproprier
	for l in range(len(file)-1):
		ligne = file[l]
		date = ligne.split("<br/>")
		date = date[0].split('.')
		date = date[1].split('-')

		if int(date[0]) == int(ref_date[0]) and int(date[1]) == int(ref_date[1]) and int(date[2]) == int(ref_date[2]) and int(date[3]) <= int(ref_date[3]) and int(date[3]) >= Min_date:
			data_actif = data_actif + ligne
	#addition des portes
	data_actif = data_actif.split(' ')
	data_actif = data_actif[1].split("<br/>")

	for l in range(len(data_actif)-1):
		data_porte = data_actif[l]
		data_porte = data_porte.split('.')
		data_porte = data_porte[0].split('-')
		if data_porte[0] == "0" or data_porte[0] == "\n0":
			Porte_1 = Porte_1 + 1
		if data_porte[1] == "0":
			Porte_2 = Porte_2 + 1
		if data_porte[2] == "0":
			Porte_3 = Porte_3 + 1
		if data_porte[3] == "0":
			Porte_4 = Porte_4 + 1
	return render_template("patron-rheure.html", heure = Nb_Heure, porte_1 = Porte_1, porte_2 = Porte_2 , porte_3 = Porte_3, porte_4 = Porte_4)

@Watchmen.route('/freq')
def Top_Port():
	fd3s = open("/home/tge/Watchmen/donne.log", 'r')
	position4 = fd3s.readlines()
	fd3s.close()

	Porte = [0,1,2,3]
	i = 0
	porte_1 = 0
	porte_2 = 0
	porte_3 = 0
	porte_4 = 0
	while i < len(position4):
		p_porte = position4[i].split(".")
		p_door = p_porte[0].split("-")
		if p_door[0] == "0":
			porte_1 = porte_1 + 1
		if p_door[1] == "0":
			porte_2 = porte_2 + 1
		if p_door[2] == "0":
			porte_3 = porte_3 + 1
		if p_door[3] == "0":
			porte_4 = porte_4 + 1
		i = i + 1

	if porte_1 > porte_2 and porte_1 > porte_3 and porte_1 > porte_4:
		Porte[0] = ("Porte 1   ", porte_1)
		Porte[1] = ("Porte 2   ", porte_2)
		Porte[2] = ("Porte 3   ", porte_3)
		Porte[3] = ("Porte 4   ", porte_4)
	if porte_2 > porte_1 and porte_2 > porte_3 and porte_2 > porte_4:
		Porte[0] = ("Porte 1   ", porte_1)
		Porte[1] = ("Porte 2   ", porte_2)
		Porte[2] = ("Porte 3   ", porte_3)
		Porte[3] = ("Porte 4   ", porte_4)
	if porte_3 > porte_1 and porte_3 > porte_2 and porte_3 > porte_4:
		Porte[0] = ("Porte 1   ", porte_1)
		Porte[1] = ("Porte 2   ", porte_2)
		Porte[2] = ("Porte 3   ", porte_3)
		Porte[3] = ("Porte 4   ", porte_4)
	if porte_4 > porte_1 and porte_4 > porte_2 and porte_4 > porte_3:
		Porte[0] = ("Porte 1   ", porte_1)
		Porte[1] = ("Porte 2   ", porte_2)
		Porte[2] = ("Porte 3   ", porte_3)
		Porte[3] = ("Porte 4   ", porte_4)

	date0 = str(p_porte[1])
	date1 = date0.split("<br/>")
	date2 = str(date1[0])

	date3 = datetime.strptime(date2, "%Y-%m-%d-%H-%M")

	Porte.sort(reverse=True, key=index)

	La_PorteNum1 = str(Porte[0])
	La_PorteNum2 = str(Porte[1])
	La_PorteNum3 = str(Porte[2])
	La_PorteNum4 = str(Porte[3])

	date4 = date3.strftime("%Y/%m/%d %H:%M")

	return render_template("patron-freqheure.html", Date = date4, Porte_1 = La_PorteNum1, Porte_2 = La_PorteNum2, Porte_3 = La_PorteNum3, Porte_4 = La_PorteNum4)

@Watchmen.route('/rapport')
def Etat_Port_actuel():
	Porte_1 = " "
	Porte_2 = " "
	Porte_3 = " "
	Porte_4 = " "
	file_porte = open("/home/tge/Watchmen/donne.log", 'r')
	donne_file = file_porte.readlines()
	file_porte.close()
	last_line = donne_file[len(donne_file)-1]
	etat_porte = last_line.split(".")
	porte = etat_porte[0].split("-")

	if porte[0] == "0":
		Porte_1 = "ouverte"
	else:
		Porte_1 = "fermer"

	if porte[1] == "0":
		Porte_2 = "ouverte"
	else:
		Porte_2 = "fermer"

	if porte[2] == "0":
		Porte_3 = "ouverte"
	else:
		Porte_3 = "fermer"

	if porte[3] == "0":
		Porte_4 = "ouverte"
	else:
		Porte_4 = "fermer"
	return render_template("patron-rapport.html", porte_1 = Porte_1, porte_2 = Porte_2, porte_3 = Porte_3, porte_4 = Porte_4)
