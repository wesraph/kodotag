"""
Ce fichier ce charge de faire le rendus graphique du niveau, des joueurs et des tirs.
"""

from __future__ import division
import res
import pygame
import threading
import Sprites 
import Camera
import Tir

class MoteurGraphique:
	def __init__(self):
		print "Lancement du moteur graphique"
		
	def Initialisation(self):
			print("Initialisation du moteur graphique")
			self.CalculerConstante()
			self.moteur = threading.Thread(None,  self.RenduGraphique, None, (1,), None)
			self.moteur.start()
			
					
	def RenduGraphique(self, a):
		print("Lancement du moteur de rendu graphique")
		while res.continuer_jeu == 1:
			res.fenetre.blit(res.fond, (0,0))
			res.niveau.afficher(res.fenetre)
			
			#On calcul la position du joueur en pixel avant l'affichage
			self.CalculerPositionJoueur()
			res.fenetre.blit(res.Sprites.getImage(), (res.character.x, res.character.y))
			
			
			#On fait le rendu des balles
			self.RenduBalles()
			
			#On fait le rendu des autres joueurs
			self.RenduJoueurs()
			
			#On affiche la minicarte
			res.interface.rendu()
			
			pygame.display.flip()
			pygame.time.Clock().tick(res.VitesseJeu)
			
	def CalculerPositionJoueur(self):
		#On calcul la position en pixel du joueur a l'ecran
		res.character.x = int(((res.character.PosX) - (Camera.PositionX)) * self.CstPPX)
		res.character.y = int(((res.character.PosY) - (Camera.PositionY)) * self.CstPPY)
		
	def CalculerPositionJoueurMulti(self, numeroJoueur): #Renvoi la position en pixel des joueurs
		return (int(((res.LPositionX[numeroJoueur]) - (Camera.PositionX)) * self.CstPPX), int(((res.LPositionY[numeroJoueur]) - (Camera.PositionY)) * self.CstPPY))
	
	def CalculerConstante(self): #Calcul la constante du nombre de pixels par bloc
		print ("Calcul de la constance Bloc/pixel")
		self.CstPPX = res.ResolutionX / Camera.NombreSpriteAEcranX
		print "CstPPX = ", self.CstPPX
		self.CstPPY = res.ResolutionY / Camera.NombreSpriteAEcranY
		
	def RenduBalles(self): #On colle les balles a l'ecran
		if(res.RenduMultijoueurs == 1):
			for i in range(0, len(Tir.LPositionX)):
				res.fenetre.blit(res.Sprites.balle, (int(((Tir.LPositionX[i]) - (Camera.PositionX)) * self.CstPPX), int(((Tir.LPositionY[i]) - (Camera.PositionY)) * self.CstPPY)))
				
	def RenduJoueurs(self): #Fonction qui fait le rendu des autres joueurs
		if(res.RenduMultijoueurs == 1): #Si le mode avec les autres joueurs est lance
			for i in range (0, res.NombreJoueurs):
				res.fenetre.blit(res.Sprites.getImageMulti(i), self.CalculerPositionJoueurMulti(i))