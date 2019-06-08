import threading
from constantes import *
import res
import pygame
import class_niveau


class MoteurPhysique:
        def __init__(self):
            print "Lancement du moteur physique"
            
        def Initialisation(self):
                print("Initialisation du moteur physique")
                self.moteur = threading.Thread(None,  self.Moteur, None, (1,), None)
                self.moteur.start()
            
        def Moteur(self, stop):
                print("Lancement de la thread du moteur physique")
                while res.continuer_jeu == 1:
				
					pygame.time.Clock().tick(res.VitesseJeu)
						
					if res.character.vitesse_x != 0 :
						#La vitesse n'est pas nulle, on fait avancer le personnage
						res.character.PosX = res.character.vitesse_x + res.character.PosX
					
					if res.character.vitesse_y != 0 :
						#La vitesse n'est pas nulle, on fait avancer le personnage
						res.character.PosY = res.character.vitesse_y + res.character.PosY