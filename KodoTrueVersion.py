import pygame
from pygame.locals import *
from class_niveau import *
import res
from class_perso import *

pygame.init()



#-----------------------------------Boucle principale-----------------------------------

continuer = 1
pygame.key.set_repeat(30, 30)

res.CreationRes()
res.InitialiserJeu()


#Boucle de jeu

while res.continuer_jeu == 1:

		pygame.time.Clock().tick(res.VitesseJeu)
		
		for event in pygame.event.get():

				if event.type == KEYDOWN:

						if event.key == K_ESCAPE:
								res.continuer_jeu = 0
								continuer = 0
						elif event.key == K_RIGHT:
								res.character.deplacer('droite')
						elif event.key == K_LEFT:
								res.character.deplacer('gauche')
						elif event.key == K_UP:
								res.character.deplacer('haut')
						elif event.key == K_DOWN:
								res.character.deplacer('bas')
								
				elif event.type == KEYUP:
						if event.key == K_RIGHT:
								res.character.deplacer('arreterdroite')
						elif event.key == K_LEFT:
								res.character.deplacer('arretergauche')
						elif event.key == K_DOWN:
								res.character.deplacer('arreterbas')
						elif event.key == K_UP:
								res.character.deplacer('arreterhaut')


		
