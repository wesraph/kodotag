import pygame
from pygame.locals import *
from constantes import *
import class_niveau
import res
import Camera

mur = 0
herbe = 0

class Niveau:
	def __init__(self, map):
		self.map = map
		self.structure = 0
		
		#On calcul les resolutions des sprites
		self.CalculerResolution()

		#Chargement des sprites
		#Bloc de mur
		
		class_niveau.mur = pygame.image.load("images/mur.png")
		class_niveau.mur = pygame.transform.scale( class_niveau.mur, (res.ResSpriteBlocX, res.ResSpriteBlocY))
		class_niveau.mur.convert()
		#Bloc d'herbe
		class_niveau.herbe = pygame.image.load("images/herbe.png")
		class_niveau.herbe = pygame.transform.scale(class_niveau.herbe, (res.ResSpriteBlocX, res.ResSpriteBlocY))
		class_niveau.herbe.convert()
		
	#Generation de la map
	def generer(self):
		with open(self.map, "r") as map:
			structure_map = []
			for ligne in map:
				ligne_map = []
				for sprite in ligne:
					if sprite != '\n':
						ligne_map.append(sprite)
						Camera.NombreSpriteTotalX = Camera.NombreSpriteTotalX + 1
				structure_map.append(ligne_map)
				Camera.NombreSpriteTotalY = Camera.NombreSpriteTotalY + 1
			self.structure = structure_map
			
			#On calcul le nombre de sprite sur l'axe Y
			Camera.NombreSpriteTotalX = (Camera.NombreSpriteTotalX / Camera.NombreSpriteTotalY) + 1
			print Camera.NombreSpriteTotalX

	#Affichage de la map
	def afficher(self, fenetre):
		num_line = 0
		num_x = 0
		num_y = 0
		for  num_y in range(Camera.NombreSpriteAEcranY) :
			num_x = 0
			for num_x in range(Camera.NombreSpriteAEcranX):
				x = num_x * res.ResSpriteBlocX
				y = num_y * res.ResSpriteBlocY
				if self.structure[Camera.PositionY + num_y][(Camera.PositionX + num_x)] == 'm':
					res.fenetre.blit(class_niveau.mur, (x,y))
				if self.structure[Camera.PositionY + num_y][(Camera.PositionX + num_x)] == 'h':
					res.fenetre.blit(class_niveau.herbe, (x,y))
				
				num_x += 1
			num_y += 1	
			
	def CalculerResolution(self):
		#On calcul la taille qu'aura les personnages a l'ecran
		res.ResSpritePersoX = int((float(res.TaillePersonnage)/float(100)) * res.ResolutionX) + 1#On est oblige de forcer le type sinon l'arrondi avec le int fait que la variable vaut 0
		res.ResSpritePersoY = int(((float(res.TaillePersonnage)/float(100)) * res.ResolutionY) / res.RatioImage) + 1
		
		#On calcul la taille des blocs a l'ecran
		res.ResSpriteBlocX = int(float(res.ResolutionX)/float(res.Camera.NombreSpriteAEcranX)) + 1
		res.ResSpriteBlocY = int(float(res.ResolutionY)/float(res.Camera.NombreSpriteAEcranY)) + 1
