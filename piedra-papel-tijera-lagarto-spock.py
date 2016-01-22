
import random
import os
t_opciones = ("PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK")

d_solucion = {"piedra":["tijera","lagarto"],"papel":["piedra","spock"],"tijera":["papel","lagarto"],"lagarto":["spock","papel"],"spock":["tijera","piedra"]} 
puntos_pc=0
puntos_user=0
while True:
	os.system("clear")
	pc = random.choice(t_opciones)
	user = raw_input ("Elige: %s " % (t_opciones,) )
	print "PC elige %s y tu elegiste %s " % (pc,user.upper())
	#print d_solucion[pc.lower()]
	if user.upper() == pc.upper():
		print "Empate"
	elif pc.lower() in d_solucion[user.lower()]:
		print "Ganaste" 
		puntos_user = puntos_user + 1
	else:
		print "Perdiste"
		puntos_pc = puntos_pc + 1
	
	print " User: %s" % ("*"*puntos_user) 
	print "   Pc: %s" % ("*"*puntos_pc)
	raw_input("Presiona ENTER para continuar")
