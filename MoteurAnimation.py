
NombreSprites = 2

class MoteurAnimation:
	def __init__(self):
		print "Creation du moteur d'animation"
	
	def Moteur(self):
		print "Lancement du moteur d'animation"
		while res.continuer_jeu == 1:
		
			pygame.time.Clock().tick(3)
			if res.Sprites.StatusPersonnage != 0:
				if res.Sprites.StatusPersonnage >= 2:
					res.Sprites.StatusPersonnage = 1
				else:
				res.Sprites.StatusPersonnage = res.Sprites.StatusPersonnage + 1