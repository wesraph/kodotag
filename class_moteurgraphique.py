import res
import pygame
import threading
import Sprites
import Camera


class MoteurGraphique:
	def __init__(self):
		print "Lancement du moteur graphique"
		
	def Initialisation(self):
			print("Initialisation du moteur graphique")
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
			pygame.display.flip()
			pygame.time.Clock().tick(res.VitesseJeu)
			
	def CalculerPositionJoueur(self):
		#On calcul la position en pixel du joueur a l'ecran
		res.character.x = int(res.character.PosX) -  float(Camera.PositionX)
		res.character.y = int(res.character.PosY) -  float(Camera.PositionY)
