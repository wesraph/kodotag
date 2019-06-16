"""
Ce fichier gere le scrolling de l'ecran lorsque le joueur arrive pres des bordures de l'ecran
"""

import res
import pygame
import threading
import Camera
import Sprites

class MoteurScrolling:
	bordure = 2
	def __init__(self):
		print "Lancement du moteur de scrolling"
		
	def Initialisation(self):
			print("Initialisation du moteur graphique")
			self.moteur = threading.Thread(None,  self.Scrolling, None, (1,), None)
			self.moteur.start()
					
	def Scrolling(self, a):
		print("Lancement du moteur de scrolling")
		while res.continuer_jeu == 1:
		
			if(res.character.x > res.ResolutionX - Sprites.ResSpritePersoX * (self.bordure + 1)):
				Camera.PositionX = Camera.PositionX + 1
			if(res.character.x < Sprites.ResSpritePersoX * self.bordure):
				Camera.PositionX = Camera.PositionX - 1
			if(res.character.y > res.ResolutionY - Sprites.ResSpritePersoY * self.bordure ):
				Camera.PositionY = Camera.PositionY + 1
			if(res.character.y < Sprites.ResSpritePersoY * self.bordure):
				Camera.PositionY = Camera.PositionY - 1
				
			pygame.time.Clock().tick(30) #Pas besoin de plus 