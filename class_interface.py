import pygame
from pygame.locals import *
from constantes import *
import class_perso
import res

class Interface:
	def __init__(self):
	
		#position joueur
		self.petitpoint = pygame.image.load("images/iconejoueur.png")
		self.petitpoint = pygame.transform.scale( self.petitpoint, (3,3))
		self.petitpoint.convert()
		
		#Minimap de fond
		self.cadre = pygame.image.load("images/minimapcadre.png")
		self.cadre = pygame.transform.scale( self.cadre, (100,100))
		self.cadre.convert()
		
		
	def Rendu(self, z):
		print("Rendu")
		self.renduX = 10
		self.renduY = 10
		
		#D'abord on affiche le cadre
		res.fenetre.blit(self.cadre, (0, res.ResolutionY - 100))
		
		#Ensuite on affiche le personnage
		res.fenetre.blit(self.petitpoint
		
		
	
		