# -*- coding: utf-8 -*-
#! /usr/bin/python
import res
import Sprites 
import pygame

#On creait un tableau de personnage
personnage =  list()
personnage.append(list())


DirectionPersonnage = 0
StatusPersonnage = 0 # 0: Personnage a l'arret 1: Pied gauche 2: Pied droite
NumeroPersonnage = 0 #Correspond au numero du skin
#Relatif a la resolution des sprites
ResSpritePersoX = 0
ResSpritePersoY = 0 



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
	
	

"""Cette fonction retourne le chemin du fichier a charger selon le numero du personnage, sa direction, et son mouvement
La table qui regit le fonctionnement est:
a = le numero du personnage
b = l'orientation du personnage qui est : 0 Haut 1 Bas 2 Gauche 3 Droite
c = Son mouvement qui est : 0 a l'arret 1 pied gauche 2 pied droit
"""
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
		Sprites.ResSpritePersoX = int((float(res.TaillePersonnage)/float(100)) * res.ResolutionX) + 1#On est oblige de forcer le type sinon l'arrondi avec le int fait que la variable vaut 0
		Sprites.ResSpritePersoY = int(((float(res.TaillePersonnage)/float(100)) * res.ResolutionY) / res.RatioImage) + 1
				
		