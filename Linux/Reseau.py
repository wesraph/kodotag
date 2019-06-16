"""
Ce ficher ce charge de synchroniser l'emplacement des joueurs et ennemis, 
leur pseudos, leurs caracteristiques...
"""

import res
import socket
import threading
import pygame
import time
import Reseau
import Tir

def Reseau():
	print "Lancement de la partie reseau"
	print "Tentative de connexion au serveur"
	res.ConServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #On creait le socket
	res.ConServeur.connect((res.AdresseIP, res.Port))
	print "Connexion etablie ! "
	print "Le niveau a charger est le numero "
	Recu = res.ConServeur.recv(1) # On receptionne le numero de la carte a charge
	Recu.decode()
	res.NiveauACharger = int(Recu) #On converti en int et on envoi dans res
	print res.NiveauACharger
	
def Initialisation():


	#On envoi notre pseudo au serveur
	EnvoyerMessage(str(res.Pseudo + " ///"))
	
	#On creait les theads d'envoi et de reception
	threadEnvoi = threading.Thread(None ,Envoi, None, (1,), None)
	threadEnvoi.start()
	threadReception = threading.Thread(None ,Reception, None, (1,), None)
	threadReception.start()
def Reception(o):
	print "Lancement de la thread de recepetion"

	
	Recu = res.ConServeur.recv(1) #On receptionne d'abord le nombre de joueurs
	Recu.decode()
	res.NombreJoueurs = int(Recu)	
	print "La partie est avec" , res.NombreJoueurs, " joueurs"
	#On creait le nombre de case dans les tableaux
	for i in range(0,res.NombreJoueurs + 1):
		res.LPositionX.append(14)
		res.LPositionY.append(14)
		res.LOrientation.append(1)
		res.LMouvement.append(1)
		res.LScore.append(0)
		res.LPseudo.append("Joueur" + str(i))
		res.LNombreVictoires.append(0)
		
	#On lance la partie 
	res.EnAttente = 0
	res.RenduMultijoueurs = 1 #On indique au reste du programme que le rendu des autres joueurs doit etre fait
	
	while res.continuer_jeu == 1:
	
		Recu = ""
		while(("///" in Recu) != 1):	
			Recu += res.ConServeur.recv(1) #On receptionne d'abord le nombre de joueurs
		Recu.decode()
		
		(Commande, NumeroJoueur, VariableA, VariableB, SertARien) = Recu.split() #On recupere chaque parametre
		if("POS1" in Commande): #On a recu une commande de position au format: "POS1 numeroJoueur X Y"
			res.LPositionX[int(NumeroJoueur)] = float(VariableA)
			res.LPositionY[int(NumeroJoueur)] = float(VariableB)
		if("POS2" in Commande): #On a recu une commande au format "POS2 numeroJoueur Orientation Mouvement"
			res.LOrientation[int(NumeroJoueur)] = int(VariableA)
			res.LMouvement[int(NumeroJoueur)] = int(VariableB)
		if("TIR" in Commande):
			FTir(int(NumeroJoueur), float(VariableA), float(VariableB)) #On utilise les memes variables que pour le deplacement
		if("VIE" in Commande): #On met a jour notre vie
			res.character.vie = int(VariableB)
			if(res.character.vie <= 0):#On est mort
				res.character.PosX = 13
				res.character.PosY = 13
		if("SCR" in Commande): #On met a jour notre score
			res.LScore[int(NumeroJoueur)] = int(VariableA)
		if("PSD" in Commande): #On change le pseudo d'un joueur
			res.LPseudo[int(NumeroJoueur)] = str(VariableA)
			print res.LPseudo[int(NumeroJoueur)] 
		if("TMP" in Commande): #On met a jour le chrono
			res.Chrono = str(VariableA)
			print res.Chrono
		if("GG" in Commande): #Un joueur vient de gagner la partie, on met a jour son score
			res.LNombreVictoires[int(NumeroJoueur)] = int(VariableA)
			
def FTir(NumeroBalle, PosX, PosY): #FTir pour FonctionTir
	if(len(Tir.LPositionX) <= NumeroBalle):
		Tir.LPositionX.append(PosX)
		Tir.LPositionY.append(PosY)
		print "Nouveau tir recu"
	else:
		Tir.LPositionX[NumeroBalle] = PosX
		Tir.LPositionY[NumeroBalle] = PosY
def Envoi(o):
	print "Lancemment de la thread d'envoi"
	while res.EnAttente == 1: #On attend tant que la partie n'est pas lancee
			time.sleep(0.5)
			
	while res.EnJeu == 1:
		#On envoi la position de notre joueur
		EnvoyerMessage("POS1 " + str(res.character.PosX) + " " + str(res.character.PosY) + " ///" )
		EnvoyerMessage("POS2 "  +  str(res.Sprites.DirectionPersonnage) + " " + str(SavoirSiMouvement()) + " ///")
		
		pygame.time.Clock().tick(40) #On l'envoi 40 fois par seconde
			
			
			
def EnvoyerMessage(Message):
	Message.encode()
	res.ConServeur.sendall(Message) #Puis on envoi le message
	
	
def StrTailleMessage(Message): #Renvoi la taille du message en string avec une taille constante de 3 caracteres
	
	Centaine = 0
	Dizaine = 0
	Unite = 0
	TailleMessage = len(Message)
	
	while(TailleMessage>100):
		Centaine+=1
		TailleMessage = TailleMessage - 100
	while(TailleMessage > 10):
		Dizaine+=1
		TailleMessage = TailleMessage -10
	while(TailleMessage > 0):
		Unite+=1
		TailleMessage = TailleMessage -1
		
	return str(str(Centaine) + str(Dizaine) + str(Unite))
	
def SavoirSiMouvement():
	if(res.Sprites.StatusPersonnage != 0):
		return 1
	else:
		return 0
	return 0
