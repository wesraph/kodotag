"""
Thread unique a chacun des  joueurs qui met a jour les positions X et Y des autres joueurs,
elle contient egalement les fonctions permettant d'envoyer des commandes aux autres joueurs 
depuis d'autres threads.
"""

import Ressources
import pygame
import time
import Envoi

def Envoi(numeroJoueur):
	print "Lancement de la thread d'envoi n" , numeroJoueur
	
	#Creation des variables du joueur
	Ressources.LPositionX.append(11)
	Ressources.LPositionY.append(11)
	Ressources.LOrientation.append(0)
	Ressources.LMouvement.append(0)
	Ressources.LPseudoJoueur.append("Joueur")
	Ressources.LEnEnvoi.append(0)
	Ressources.LVie.append(4)
	Ressources.LScore.append(0)
	Ressources.LVictoire.append(0)
	
	#On attend deux secondes pour que toutes les threads soient crees
	time.sleep(2)
	
	if(Ressources.PseudoDejaEnvoye == 0):
		Ressources.PseudoDejaEnvoye = 1
		print "Envoi des pseudos"
		EnvoiPseudo()
		
	while Ressources.EnJeu == 1:
	
		#Envoi des positions de joueurs
		for i in range(0, Ressources.NombreJoueursConnectes):
			#Envoi du numero de joueur, la position X et Y, de l'orientation et de si le personnage bouge
			if(i != numeroJoueur):
			
				#On envoi la position du joueur
				EnvoyerMessage("POS1 " + str(i) + " " + str(Ressources.LPositionX[i]) + " "+
				str(Ressources.LPositionY[i]) + " ///", numeroJoueur) 
				EnvoyerMessage("POS2 "+ str(i) + " " + str(Ressources.LOrientation[i]) + " " +
				str(Ressources.LMouvement[i]) + " ///", numeroJoueur)
			
		pygame.time.Clock().tick(40)

def EnvoyerMessage(Message, numeroJoueur): #Envoi le message au joueur
	while Ressources.LEnEnvoi[numeroJoueur] == 1: #Tant qu'une autre thread est en train d'envoyer, on attend 
		1==1
	Ressources.EnEnvoi = 1
	#Ressources.Lsocket[numeroJoueur].send(StrTailleMessage(Message).encode())  
	Message.encode()
	Ressources.Lsocket[numeroJoueur].send(Message)
	Ressources.LEnEnvoi[numeroJoueur] = 0


def BroadcastMessage(Message): #Fonction qui envoi a tous les joueurs le message
	for u in range(0, Ressources.NombreJoueursConnectes):
		EnvoyerMessage(Message, u)
		
		
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
	
	return str(str(Centaine) + str(Dizaine) + str(Unite) + " ")

def EnvoiPseudo(): 
	for i in range(0, Ressources.NombreJoueursConnectes):
		BroadcastMessage(str("PSD " + str(i) + " " + str(Ressources.LPseudo[i]) +" 0 ///"))

			
#Protocole
#Envoi d'une position: "POS Joueur X Y"