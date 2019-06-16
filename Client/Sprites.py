"""
Gere les sprites, ainsi que leurs chargements
"""

from __future__ import division
import res
import Sprites
import pygame
import Camera
#On creait un tableau de personnage
personnage =  list()
personnage.append(list())

balle = 0

DirectionPersonnage = 0
StatusPersonnage = 0 # 0: Personnage a l'arret 1: Pied gauche 2: Pied droite
NumeroPersonnage = 0 #Correspond au numero du skin
#Relatif a la resolution des sprites
ResSpritePersoX = 0
ResSpritePersoY = 0 
ResSpriteBalleX = 0
ResSpriteBalleY = 0



def ChargerSpritePersonnage():
	print "Chargement des sprites du personnage"
	
	#Calcul de la resolution du blitage des personnages
	CalculerResolution()
	#Creation du tableau de personnage
	CreerPersonnageSprite()
	#On ne charge que l'image 0 pour le moment
	for i in range(0,4):
		for u in range(0,3):
			Sprites.personnage[i].append(pygame.image.load(Sprites.StringPersonnage(NumeroPersonnage,i,u)))
			Sprites.personnage[i][u] = pygame.transform.scale(Sprites.personnage[i][u],(Sprites.ResSpritePersoX,Sprites.ResSpritePersoY))
			Sprites.personnage[i][u].convert()
	print "Fin de chargement des sprites du personnage"
	
	#On charge le sprite de la balle
	Sprites.balle = pygame.image.load("images//balle.png")
	Sprites.balle = pygame.transform.scale(Sprites.balle, (Sprites.ResSpriteBalleX, Sprites.ResSpriteBalleY))
	Sprites.balle.convert()
	
"""Cette fonction retourne le chemin du fichier a charger selon le numero du personnage, sa direction, et son mouvement
La table qui regit le fonctionnement est:
a = le numero du personnage
b = l'orientation du personnage qui est : 0 Haut 1 Bas 2 Gauche 3 Droite
c = Son mouvement qui est : 0 a l'arret 1 pied gauche 2 pied droit
"""

def getImageMulti(numeroPersonnage): #Retourne l'image a binder du personnage (multijoueurs)
	return Sprites.personnage[res.LOrientation[numeroPersonnage]][res.LMouvement[numeroPersonnage]]
	
def StringPersonnage(a,b,c):
	d = str("images//personnages//")+str(a)+"-"+str(b)+"-"+str(c)+".png"
	return d
	
def CreerPersonnageSprite():
	for i in range(0,3):
		Sprites.personnage.append(list())

#Meme fonctionnement que pour la fonction StringPersonnage, mais retourne l'image a binder
def getImage():
		return Sprites.personnage[Sprites.DirectionPersonnage][Sprites.StatusPersonnage]
		
def CalculerResolution():
		#On calcul la taille qu'aura les personnages a l'ecran
		Sprites.ResSpritePersoX = int(res.ResolutionX/Camera.NombreSpriteAEcranX * res.TaillePersonnage)
		Sprites.ResSpritePersoY = int(res.ResolutionY/Camera.NombreSpriteAEcranX * res.TaillePersonnage / res.RatioImage)
		Sprites.ResSpriteBalleX = int(res.ResolutionX/Camera.NombreSpriteAEcranX * res.TailleBalle)
		Sprites.ResSpriteBalleY = int(res.ResolutionY/Camera.NombreSpriteAEcranY * res.TailleBalle)

		