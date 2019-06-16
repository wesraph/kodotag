"""
Ce fichier contient toute les variables importantes du jeu comme les threads et les classes.
C'est egalement ce fichier qui crer toute les threads et ce charge du bon fonctionnement du jeu.
"""

import class_perso
import class_niveau
import class_moteurphysique 
import class_moteurgraphique
import pygame
import res
import Sprites
import Camera
import class_moteuranimation
import class_moteurscrolling
import class_interface
import Reseau
import Tir


#Variable qui contiennent les threads 
fenetre = 0
niveau = 0
character = 0
stop = 0
moteurphysique = 0
moteurgraphique = 0
moteuranimation = 0
moteurscrolling = 0
fond = 0
sprites = 0

#Autres
continuer_jeu = 1
VitesseJeu  = 30 #Definit le nombre d'images par seconde voulu

#Relatif a la partie reseau
AdresseIP = "10.42.0.1"
Port = 1236
ConServeur = 0 #Le socket qui permet la connexion
EnEnvoi = 0 #Variable qui permet de synchroniser les envois

#Variables qui indiquent si on est encore dans la salle d'attente et encore dans la partie
EnAttente = 0
EnJeu = 1
Pseudo = "Joueur" #Le pseudo par defaut

#Variables qui stockent les caracteristiques des autres joueurs
NombreJoueurs = 0
Chrono = 60
RenduMultijoueurs = 0 #Indique si le rendu des autres personnages doit etre fait
LPositionX = list() #Ce sont les positions X et Y des personnages
LPositionY = list()
LOrientation = list() #Indique l'orientation du personnage
LMouvement = list() #Indique si le personnage est en mouvement
LScore = list()
LNombreVictoires = list()
LPseudo = list()

#Relatif aux cartes
NiveauACharger = 2 #On le met par defaut a 2 pour 

#Resolution de l'ecran
ResolutionX = 640		
ResolutionY = 480

#Resolution des blocs en X et Y
ResSpriteBlocX = 0
ResSpriteBlocY = 0

TaillePersonnage = 2 #Correspond a la taille en bloc du personnage
RatioImage = float(float(8)/float(11)) #Ratio de la resolutionX sur la resolutionY du personnage
TailleBalle = 0.5

def CreationRes():
	print("Creation de la classe Ressources")
	#On creait ici les variables
	res.fenetre = pygame.display.set_mode((res.ResolutionX, res.ResolutionY))
	res.continuer_jeu = 1 #Variable qui indique si le jeu est en cours
    
	#On charge la partie reseau
	Reseau.Reseau()
	#On charge les sprites avant tout
	Sprites.ChargerSpritePersonnage()
    #Creation des autres classes
	res.niveau = class_niveau.Niveau("n3") #Doit etre avant character car c'est ici qu'on calcul les resolution du personnage
	res.character = class_perso.Perso()
	res.interface = class_interface.Interface()
	#Creation des moteurs graphique et physique 
	res.moteurphysique = class_moteurphysique.MoteurPhysique()
	res.moteurgraphique = class_moteurgraphique.MoteurGraphique()
	res.moteuranimation = class_moteuranimation.MoteurAnimation()
	res.moteurscrolling = class_moteurscrolling.MoteurScrolling()
	
    #Images
	res.fond = pygame.image.load("images/fond.jpg").convert()

def InitialiserJeu():
	print("Initialisation du jeu")

    #On initialise le niveau
	res.niveau.generer()
	res.niveau.afficher(fenetre)

    #On initialise le moteur physique
	res.moteurphysique.Initialisation()
	res.moteurgraphique.Initialisation()
	res.moteuranimation.Initialisation()
	res.moteurscrolling.Initialisation()
	Reseau.Initialisation()