import res
import threading
import pygame
NombreSprites = 2

class MoteurAnimation:
	def __init__(self):
		print "Creation du moteur d'animation"
	
	def Initialisation(self):
		self.moteur = threading.Thread(None,  self.MoteurAnimation, None, (1,), None)
		self.moteur.start()
	def MoteurAnimation(self, a):
		print "Lancement du moteur d'animation"
		while res.continuer_jeu == 1:
		
			pygame.time.Clock().tick(3)
			if res.character.vitesse_x != 0 or res.character.vitesse_y != 0:
				if res.Sprites.StatusPersonnage >= 2:
					res.Sprites.StatusPersonnage = 1
				else:
					res.Sprites.StatusPersonnage = res.Sprites.StatusPersonnage + 1
			else:
				res.Sprites.StatusPersonnage = 0