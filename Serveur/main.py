#Les importations
import socket
import threading
from Reseau import *
from Ressources import *
from SalleAttente import *

#On demarre le programme ici
print("Demarrage du programme serveur")
#On demarre la salle d attente
CreerSalleAttente()

#On ferme les socket pour liberer le port
for i in range(0, NombreJoueursConnectes):
	Ressources.Lsocket[i].close()
	
#On ferme le socket principal
Ressources.SocketPrincipal[0].close()
print "Extinction du jeu"