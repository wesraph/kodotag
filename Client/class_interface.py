"""
Ce fichier va creer une partie de l'interface graphique et en afficher la totalite qui est compose,
de la mini carte, des pseudos des joueurs, des scores et du temps restant pour la manche
"""

import pygame
from pygame.locals import *
from constantes import *
import class_perso
import res
import Camera
import pygame
import threading
import Tir
import Reseau

class Interface:
	def __init__(self):
	
		#position joueur
		self.petitpoint = pygame.image.load("images/iconejoueur.gif")
		self.petitpoint = pygame.transform.scale( self.petitpoint, (7,7))
		self.petitpoint.convert()
		
		#position autres joueurs
		self.petitpointEnnemi = pygame.image.load("images/iconejoueurEnnemi.gif")
		self.petitpointEnnemi = pygame.transform.scale( self.petitpointEnnemi, (7,7))
		self.petitpointEnnemi.convert()

		#position des balles
		self.balle = pygame.image.load("images/iconeballe.gif")
		self.balle = pygame.transform.scale( self.balle, (2,2))
		self.balle.convert()
		
		#Minimap de fond
		self.cadre = pygame.image.load("images/minimapcadre.png")
		self.cadre = pygame.transform.scale( self.cadre, (100,100))
		self.cadre.convert()
		

	def rendu(self):
		self.renduX = 10
		self.renduY = 10
		
		#D'abord on affiche le cadre
		res.fenetre.blit(self.cadre, (0,0))
	
		#Ensuite on affiche le personnage
		res.fenetre.blit(self.petitpoint, (((res.character.PosX/res.Camera.NombreSpriteTotalX)*100), (res.character.PosY/res.Camera.NombreSpriteTotalY)*100))
		for i in range(0, res.NombreJoueurs):
			res.fenetre.blit(self.petitpointEnnemi, (((res.LPositionX[i]/res.Camera.NombreSpriteTotalX)*100), (res.LPositionY[i]/res.Camera.NombreSpriteTotalY)*100))
		
		#Ensuite on affiche les balles
		for i in range(0, len(Tir.LPositionX)):
			res.fenetre.blit(self.balle, (((res.Tir.LPositionX[i]/res.Camera.NombreSpriteTotalX)*100), (res.Tir.LPositionY[i]/res.Camera.NombreSpriteTotalY)*100))
		
		#Ensuite on affiche la barre de vie
		
		#Full vie
		if res.character.vie == 0:
			self.barreVie = pygame.image.load("images/barrevie4.gif")
			self.barreVie = pygame.transform.scale( self.barreVie, (300,30))
			self.barreVie.convert()

		#3 vies
		if res.character.vie == 1:
			self.barreVie = pygame.image.load("images/barrevie1.gif")
			self.barreVie = pygame.transform.scale( self.barreVie, (300,30))
			self.barreVie.convert()

		#2 vies
		if res.character.vie == 2:
			self.barreVie = pygame.image.load("images/barrevie2.gif")
			self.barreVie = pygame.transform.scale( self.barreVie, (300,30))
			self.barreVie.convert()

		#1 vie
		if res.character.vie == 3:
			self.barreVie = pygame.image.load("images/barrevie3.gif")
			self.barreVie = pygame.transform.scale( self.barreVie, (300,30))
			self.barreVie.convert()
		
		#il meurt
		if res.character.vie == 4:
			#on le remet au spawn
			res.character.PosX = 13
			res.character.PosY = 13
			#on lui redonne de la vie
			res.character.vie = 0
			
		res.fenetre.blit(self.barreVie, (250, 0))
			
		
		#Afficher les pseudos
		text= pygame.font.Font(None,15)
		for i in range(0, len(res.LPseudo)):
			res.fenetre.blit(text.render(res.LPseudo[i],1,(0,0,0)),(0,110 + (i * 10)))
		
		#Afficher les scores
		for i in range(0, len(res.LScore)):
			res.fenetre.blit(text.render(str(res.LScore[i]),1,(255,0,0)),(len(res.LPseudo[i])* 6 + 15,110 + (i * 10)))
			res.fenetre.blit(text.render(str(res.LNombreVictoires[i]),1,(0,0,255)),(len(res.LPseudo[i])* 6 +  5,110 + (i * 10)))

		#Affichage du chrono
		res.fenetre.blit(text.render(str("Temps restant : " + str(res.Chrono)),1,(255,0,0)),(res.ResolutionX - 100,0))
