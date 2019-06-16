"""
Ce fichier va gerer les collisions du personnage avec les murs
"""

from __future__ import division
import res
import Collision

Bloquant = ['m']#Liste qui contient les bloc bloquant
def Collision():

	Collision.bloc0 = res.character.PosY
	Collision.bloc1 = res.character.PosY + res.TaillePersonnage
	Collision.bloc2 = res.character.PosX
	Collision.bloc3 = res.character.PosX + res.TaillePersonnage
	Collision.bloc4 = res.character.PosY + (res.TaillePersonnage/2)
	Collision.bloc5 = res.character.PosX + (res.TaillePersonnage/2)
	
	if(EstBloquant(res.niveau.structure[int(Collision.bloc0)][int(Collision.bloc2)])): #Tete gauche
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc1)][int(Collision.bloc2)])): #Pied gauche
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc0)][int(Collision.bloc3)])): #Tete droite
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc1)][int(Collision.bloc3)])): #Pied droit
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc4)][int(Collision.bloc2)])): #Cote gauche
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc4)][int(Collision.bloc3)])): #Cote droit
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc0)][int(Collision.bloc5)])): #Tete haut
		return 1
	if(EstBloquant(res.niveau.structure[int(Collision.bloc1)][int(Collision.bloc5)])): #Pied bas
		return 1
		
	return 0
			
	

	
	
	
def EstBloquant(Type): #Fonction qui verifie si le bloc envoyer est bloquant ou non
	for i in range(0, len(Bloquant)):
		if Type == Bloquant[i]:
			return 1
		
	return 0
	
	
	
	
	
	
	
	
	
	
	
#On garde pour la partie serveur est la gestion des balles	
"""
def EstEnCollisionObjet(ApositionX, ApositionY, Alargeur, Alongeur, BpositionX, BpositionY, Blargeur, Blongueur):

	if(BpositionX >= ApositionX or
	(BpositionX + Blargeur ) <= ApositionX or
	BpositionY >= (ApositionY + Alongueur) or
	(BpositionY + Blongueur) <= ApositionY): #Si il y a pas collision
		return 0
	else:
		return 1
	
	
	
def EstEnCollision():
	#On a 4 bloc a tester, ceux dessus, dessous, a gauche a droite
	if EstEnCollisionObjet(res.character.PosX, res.character.PosY, res.TaillePersonnage, (res.TaillePersonnage / res.RatioImage),
	res.character.PosX, res.character.PosY, 1, 1) == 1:
		print "aaaa"
"""