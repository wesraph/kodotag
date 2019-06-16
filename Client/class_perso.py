"""
C'est ici que sont initialisees les variables du personnage et qu'est traite
l'appuis des touches
"""

import pygame
from pygame.locals import *
from constantes import *
import res

class Perso:
	def __init__(self):
			
		self.x = 0 #La position sur l'ecran
		self.y = 0 #La position sur l'ecran
		self.direction = 0
		self.vitesse_x = 0
		self.vitesse_y = 0
		self.vitesse_max = 0.3
		self.PosX = 13 #La position dans le monde
		self.PosY = 13 #La position dans le monde
		self.vie = 0
		self.score = 0 #Son nombre de kill


	def deplacer(self, direction):
		#Deplacement vers la droite
		if direction == 'droite':
			res.Sprites.DirectionPersonnage = 3
			self.vitesse_x = self.vitesse_max

		#Deplacement vers la gauche
		if direction == 'gauche':
			res.Sprites.DirectionPersonnage = 2
			self.vitesse_x = -self.vitesse_max

		#Deplacement vers le haut
		if direction == 'haut':
			res.Sprites.DirectionPersonnage = 0
			self.vitesse_y = -self.vitesse_max

		#Deplacement vers le bas
		if direction == 'bas':
			res.Sprites.DirectionPersonnage = 1
			self.vitesse_y = self.vitesse_max

		#Arreter des deplacements
		if direction == 'arreterbas':
			self.vitesse_y = 0
		if direction == 'arreterhaut':
			self.vitesse_y = 0
		if direction == 'arretergauche':
			self.vitesse_x = 0
		if direction == 'arreterdroite':
			self.vitesse_x = 0
