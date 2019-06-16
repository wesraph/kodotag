"""
Thread qui permet de faire durer la partie 
une certaine duree et de comptabiliser les 
parties gagnees par chacun des  joueurs.
"""

import time
import Envoi
import Ressources
import Chrono


def Timer(SertARien): #Timer qui gere la session en cours
	while (1 ==1):
		temps = 60
		time.sleep(5)
		while (temps > 0):
			temps-=1
			time.sleep(1)
			Envoi.BroadcastMessage(str("TMP " + " 0 " + str(temps) + " 0 ///"))
		Chrono.TrouverGagnant() #On cherche le gagnant
	
def TrouverGagnant(): #Fonction  qui trouve le gagnant, lui ajoute un point et actualise son score chez les autres joueurs
	Gagnant = 0
	for i in range(0,Ressources.NombreJoueursConnectes):#On cherche le gagnant
		if(Ressources.LScore[i] > Gagnant):
			Gagnant = i
	Ressources.LVictoire[i]+=1 #On ajoute un point au gagant
	Envoi.BroadcastMessage(str("GG " + str(Gagnant) + " " + str(Ressources.LVictoire[Gagnant]) + " 0 ///"))
	
	#On reinitialise les scores et on envoi aux joueurs
	for i in range(0, Ressources.NombreJoueursConnectes):
		Ressources.LScore[i] = 0
		Envoi.BroadcastMessage(str("SCR " + str(i) + " " + str(Ressources.LScore[i]) + " 0 ///"))
