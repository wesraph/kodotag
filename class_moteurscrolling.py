import res
import pygame
import threading
import Camera
import Sprites
class MoteurScrolling:
	def __init__(self):
		print "Lancement du moteur de scrolling"
		
	def Initialisation(self):
			print("Initialisation du moteur graphique")
			self.moteur = threading.Thread(None,  self.Scrolling, None, (1,), None)
			self.moteur.start()
					
	def Scrolling(self, a):
		print("Lancement du moteur de scrolling")
		azerty = 0
		while res.continuer_jeu == 1:
		
			if(res.character.x > res.ResolutionX - Sprites.ResSpritePersoX):
				Camera.PositionX = Camera.PositionX + 1
			if(res.character.x < Sprites.ResSpritePersoX):
				Camera.PositionX = Camera.PositionX - 1
			if(res.character.y > res.ResolutionY - Sprites.ResSpritePersoY ):
				Camera.PositionY = Camera.PositionY + 1
			if(res.character.y < Sprites.ResSpritePersoY):
				Camera.PositionY = Camera.PositionY - 1
				
			pygame.time.Clock().tick(10) #Pas besoin de plus 