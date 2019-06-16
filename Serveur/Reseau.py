"""
Regroupe les fonctions utiles a l'initialisation de la partie reseau  et gere 
la connexion des clients au serveur. C'est egalement ici que sont creees les 
threads de reception et d'envoi de chacun des  joueurs
"""

import Ressources
import socket
import threading
import time
import Envoi
import Reception
import Reseau

#On creer le socket principal
SocketPrincipal = list()
def InitialiserConnexion(): # Initialise le socket principal
	print("Creation du socket")
	Ressources.SocketPrincipal.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	Ressources.SocketPrincipal[0].bind(("",Ressources.Port))
	Ressources.SocketPrincipal[0].listen(5)
	
	
def CreationJoueur(): #Creer les nouveaux joueurs
	#numeroJoueur est la variable qui indique a la thread son numero
	numeroJoueur = Ressources.NombreJoueursConnectes
	print("En attente d'un joueur n ", numeroJoueur)
	
	ThreadEnCours = threading.Thread(None,  AttendreConnexion, None, (numeroJoueur,), None)
	ThreadEnCours.start() 
	
	
	while Ressources.EnAttente == 1 and ThreadEnCours.isAlive(): #Voir explication n1 en bas de page
		time.sleep(0.5)
		
	if Ressources.EnAttente == 0:  #Tant qu'on attend des nouveaux joueurs on ne kill pas la thread
		ThreadEnCours._Thread__stop()
		print("On quitte CreationJoueur apres avoir kill la thread de AttendreConnexion")
		return 0
	
	print("Un client vient de ce connecter")
	Ressources.LThread.append(threading.Thread(None, Joueur, None, (numeroJoueur,), None))
	Ressources.LThread[numeroJoueur].start()
	Ressources.NombreJoueursConnectes  += 1#On incremente le nombre de joueurs connectes

def AttendreConnexion(numeroJoueur): #On ecoute sur le port en attente d'une connexion
	print("Creation de attendre connexion")
	connexionClient, infos_connexion = Ressources.SocketPrincipal[0].accept()
	Ressources.Lsocket.append(connexionClient)
	print("Fin de la thread AttendreConnexion")
		
def Joueur(numeroJoueur): #Fonction general qui gere le tout
	print("Creation de la thread  Joueur")
	
	#On envoi au joueur le numero de la carte a charger
	Ressources.Lsocket[numeroJoueur].send(str(Ressources.NumeroDeCarte).encode())
	while Ressources.EnAttente == 1:
		time.sleep(0.5)
		
	#On informe le client du nombre de joueurs connecte
	Ressources.Lsocket[numeroJoueur].send(str(Ressources.NombreJoueursConnectes).encode())
	Reception.ReceptionPseudo(numeroJoueur) #On receptionne le pseudo du joueur
	time.sleep(0.5) #On attend que tous les pseudos soient recu
	print("LANCEMENT DE LA PARTIE")
	
	#Lancement de la thread d'envoi
	Ressources.LThreadEnvoi.append(threading.Thread(None, Envoi.Envoi, None, (numeroJoueur,),None))
	time.sleep(0.5)
	Ressources.LThreadEnvoi[numeroJoueur].start()
	
	#Lancement de la thread de reception
	Ressources.LThreadReception.append(threading.Thread(None, Reception.Reception, None, (numeroJoueur,),None))
	time.sleep(0.5)
	Ressources.LThreadReception[numeroJoueur].start()

	
	"""
	Explication n1:Comme la fonction d'attente d'un client est bloquante, on la met dans une thread 
	qu'on tue lorsque le depart du jeu est lance, grace a cela le nombre de joueurs
	n'est pas fixe"""