"""
Contient la premiere fonction executee et qui lance
le reste du programme. Elle peut etre consideree comme
le "main" du programme
"""

from Ressources import *
from Reseau import *
import class_moteurphysique
import Chrono
import time
moteurphysique = 0
chrono = 0

def CreerSalleAttente(): #Creer la salle d'attente
	#Declaration des variables qu'on va utiliser
	
	print("Creation de la salle d'attente")
	
	
	#On demarre le socket principal	
	InitialiserConnexion()
	a  = threading.Thread(None, MettreAttenteGo, None, (1,), None)
	a.start()
	while Ressources.EnAttente == 1:
		CreationJoueur()
	print "On lance le jeu !"

	#On lance le moteur physique
	moteurphysique = class_moteurphysique.MoteurPhysique()
	moteurphysique.Initialisation()
	chrono = threading.Thread(None, Chrono.Timer, None, (0,), None)
	chrono.start()
	
