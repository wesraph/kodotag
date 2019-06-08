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

fenetre = 0
continuer_jeu = 1
niveau = 0
character = 0
stop = 0
moteurphysique = 0
moteurgraphique = 0
moteuranimation = 0
moteurscrolling = 0
fond = 0
sprites = 0
VitesseJeu  = 30 #Definit le nombre d'images par seconde voulu

#Relatif aux cartes
TailleCarteMonde = 1000

#Resolution de l'ecran
ResolutionX = 800
ResolutionY = 600

#Lien vers les images contenant les images du personnage joueur

ResSpriteBlocX = 0
ResSpriteBlocY = 0

TaillePersonnage = 5 #Correspond au pourcentage de taille du personnage par rapport a la resolution
RatioImage = float(float(8)/float(11)) #Ratio de la resolutionX sur la resolutionY du personnage

def CreationRes():
	print("Creation de la classe Ressources")
	#On creait ici les variables
	res.fenetre = pygame.display.set_mode((res.ResolutionX, res.ResolutionY))
	res.continuer_jeu = 1 #Variable qui indique si le jeu est en cours
    
	#On charge les sprites avant tout
	Sprites.ChargerSpritePersonnage()
	#Sprites.ChargerSpritePersonnageMini()
    #Creation des autres classes
	res.niveau = class_niveau.Niveau("n2") #Doit etre avant character car c'est ici qu'on calcul les resolution du personnage
	res.character = class_perso.Perso()
	#Creation des moteurs graphique et physique
	res.moteurphysique = class_moteurphysique.MoteurPhysique()
	res.moteurgraphique = class_moteurgraphique.MoteurGraphique()
	res.moteuranimation = class_moteuranimation.MoteurAnimation()
	res.moteurscrolling = class_moteurscrolling.MoteurScrolling()
	
    #Images
	res.fond = pygame.image.load("images/fond.jpg").convert()
    
    #Autres
	
	print "BlocX = ", res.ResSpriteBlocX , res.ResSpriteBlocY

	
	


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

	
