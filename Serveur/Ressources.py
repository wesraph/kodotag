"""
Fichier qui contient toutes les variables importantes 
et qui ont besoin d'etre accedees 
depuis les autres fichiers facilement.
Il contient egalement les threads des autres fonctions
"""


import time
import Ressources

Port = 1236 #Port de connexion
#Liste des sockets
Lsocket  = list()
Linfos = list()
SocketPrincipal = list() 
NombreJoueursConnectes = 0
LThread = list()
LThreadEnvoi = list()
LThreadReception = list()

#Variable relatives au jeu en general
VitesseJeu = 30 #Nombre de FPS
continuer_jeu = 1 
NumeroDeCarte = 5 #Le numero de la carte a charger
TailleBalle = 0.5 #La taille des balles en case
TaillePersonnage = 2 #La taille du personnage en case
LongueurPersonnage = 2.75 #Longueur du personnage en case

#Variable pour SalleAttente
EnAttente = 1 #Variable qui continue a attendre des joueurs tant qu'on ne lance pas la partie
EnJeu = 1 #Variable qui indique si le jeu est toujours en cours

#Variables des joueurs
LPositionX = list()
LPositionY = list()
LPseudoJoueur = list()
LOrientation = list()
LMouvement = list() #Tableau qui indique si le personnage est en mouvement
LEnEnvoi = list() #Tableau qui sert a synchroniser les envois

#Tableau des joueurs
#Tableau des tirs
LTirX = list()
LTirY = list()
LAccX = list()
LAccY = list()

LTireur = list() #Tableau qui stocke qui est le tireur
LVie = list() #Taleau qui  stockela vie
LPseudo = list() #Tableau qui stocke le pseudo
LScore = list() #Tableau qui stocke le pseudo
LVictoire = list() #Tableau qui stocke le nombre de victoires
PseudoDejaEnvoye = 0 #Indique si les pseudos sont deja envoye

VitesseBalle = 0.5 #Definit la vitesse des balles

#Variable qui indique si on est en train de
#modifier le tableau, utile pour la synchronisation des threads
EnChangement = 0 

def IncrementerNombreJoueursConnectes():
	NombreJoueursConnectes = NombreJoueursConnectes + 1

def MettreAttenteGo(a): #Chrono qui sert a passer de l'attente de joueurs au lancement de la partie
	print("En attente du lancement de la partie")
	Attente = input("Appuyez sur une touche pour lancer la partie")
	Ressources.EnAttente = 0
	print("Lancement de la partie ")
