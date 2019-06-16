"""
Gere la collision des balles avec les murs et les personnages.
C'est egalement ce moteur qui permet aux balles d'avancer.
"""


import threading
import Ressources
import pygame
import Envoi

class MoteurPhysique:

	Bloquant = ['m']#Liste qui contient les bloc bloquant
	
	#La map qui va contenir chaque blocs
	map = 0
	structure = 0
	
	#Definit la taille max de la map. Ceci est calcule pendant le chargement du niveau
	TailleMaxX = 0
	TailleMaxY = 0
	
	#Les blocs utilises dans la fonction gerant la collision avec les murs
	bloc0 = 0
	bloc1 = 0
	bloc2 = 0
	bloc3 = 0
	bloc4 = 0
	bloc5 = 0
	
	def __init__(self):
		print "Creation du moteur physique"
		
	def Initialisation(self):
			print("Initialisation du moteur physique")
			self.generer() #On charge la carte en memoire
			self.moteur = threading.Thread(None,  self.Moteur, None, (1,), None)
			self.moteur.start()	
		
	def generer(self): #Fonction reprise dans le code client
		print "Chargement du niveau "
		with open(self.NomNiveau(), "r") as map:
			structure_map = []
			for ligne in map:
				ligne_map = []
				for sprite in ligne:
					if sprite != '\n':
						ligne_map.append(sprite)
						self.TailleMaxX+=1
				structure_map.append(ligne_map)
				self.TailleMaxY+=1
			self.structure = structure_map
		self.TailleMaxX = (self.TailleMaxX / self.TailleMaxY)
		print "TailleMaxX" , self.TailleMaxX
		print "TailleMaxY", self.TailleMaxY
		print "OK"
				
			
	def NomNiveau(self): #Retourne le nom du niveau selon le numero de la carte
		return str(str("n") + str(Ressources.NumeroDeCarte))
	
	def Moteur(self, stop): #Thread du moteur physique
			print("Lancement de la thread du moteur physique")
			while Ressources.continuer_jeu == 1:
				for i in range(0, len(Ressources.LTirX)):
				
					if(Ressources.LTirX[i] != 0 or Ressources.LTirY[i] != 0):
					
						if(Ressources.LAccX[i] != 0):
							Ressources.LTirX[i] = float(Ressources.LTirX[i]) + float(Ressources.LAccX[i])
							
						if(Ressources.LAccY[i] != 0):
							Ressources.LTirY[i] = float(Ressources.LTirY[i]) + float(Ressources.LAccY[i])
						
					#Maintenant qu'on a fait avancer la balle, on test la collision
					self.Collision(i)
					
				self.EnvoiTir()
				pygame.time.Clock().tick(Ressources.VitesseJeu)

	def Collision(self, numeroBalle):
		#On test d'abord le mur
		if (self.CollisionMur(numeroBalle) == 1):
			self.EffacerBalle(numeroBalle)
		self.CollisionPersonnage(numeroBalle)
						
	def EffacerBalle(self, numeroBalle):
		Ressources.LTirX[numeroBalle] = 0
		Ressources.LTirY[numeroBalle] = 0
		Ressources.LAccX[numeroBalle] = 0
		Ressources.LAccY[numeroBalle] = 0
		Ressources.LTireur[numeroBalle] = 0
	
	def CollisionPersonnage(self, numeroBalle): #Fonction qui fait les collisons balles/personnages
		
		for i in range(0,Ressources.NombreJoueursConnectes):
			if(float(Ressources.LTirX[numeroBalle]) >= float(Ressources.LPositionX[i]) + float(Ressources.TaillePersonnage) or
			float(Ressources.LTirX[numeroBalle]) + Ressources.TailleBalle <= float(Ressources.LPositionX[i]) or
			float(Ressources.LTirY[numeroBalle]) >= (float(Ressources.LPositionY[i]) + float(Ressources.LongueurPersonnage)) or
			float(Ressources.LTirY[numeroBalle]) + Ressources.TailleBalle <= float(Ressources.LPositionY[i])): #Si il y a pas collision
			#On ne fait rien
							1==1 #On met un code inutile ici pour que la condition soit prise en compte
			
			else:
				print "Collision Personnage"
				if(Ressources.LTireur[numeroBalle] != i): #Le touche n'est pas le tireur
					self.Touche(i, numeroBalle)
		
		
	def CollisionMur(self,numeroBalle): #Fonction qui fait les collisions balles/murs
		self.bloc0 = float(Ressources.LTirY[numeroBalle])
		self.bloc1 = float(Ressources.LTirY[numeroBalle]) + Ressources.TailleBalle
		self.bloc2 = float(Ressources.LTirX[numeroBalle])
		self.bloc3 = float(Ressources.LTirX[numeroBalle]) + Ressources.TailleBalle
		self.bloc4 = float(Ressources.LTirY[numeroBalle])+ (Ressources.TailleBalle/2)
		self.bloc5 = float(Ressources.LTirX[numeroBalle]) + (Ressources.TailleBalle/2)
		
		if(self.EstBloquant(self.structure[int(self.bloc0)][int(self.bloc2)])): #Tete gauche
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc1)][int(self.bloc2)])): #Pied gauche
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc0)][int(self.bloc3)])): #Tete droite
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc1)][int(self.bloc3)])): #Pied droit
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc4)][int(self.bloc2)])): #Cote gauche
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc4)][int(self.bloc3)])): #Cote droit
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc0)][int(self.bloc5)])): #Tete haut
			return 1
		if(self.EstBloquant(self.structure[int(self.bloc1)][int(self.bloc5)])): #Pied bas
			return 1
		return 0
		
		
	def EstBloquant(self, Type): #Fonction qui verifie si le bloc envoyer est bloquant ou non
		for i in range(0, len(self.Bloquant)):
			if Type == self.Bloquant[i]:
				return 1
		return 0
		
	def Touche(self, i, numeroBalle): #Fonction qui gere les collisons joueurs/balle
		Ressources.LVie[i]= Ressources.LVie[i] - 1 #On retire un point de vie 
		self.EnvoiVie(i) #On envoi la nouvelle vie aux joueurs
		Ressources.LScore[Ressources.LTireur[numeroBalle]]+= 1 #On incremente le score
		#On envoi le score a tous les joueurs
		Envoi.BroadcastMessage(str("SCR " +  str(Ressources.LTireur[numeroBalle]) +  " " + str(Ressources.LScore[Ressources.LTireur[numeroBalle]]) + " 0 ///"))
		self.EffacerBalle(numeroBalle) #On efface la balle	
		
	def EnvoiTir(self):#Envoi a tous les joueurs la position des balles
			for i in range(0, len(Ressources.LTirX)): #On envoi toutes les positions de tir a tous les joueurs
				Envoi.BroadcastMessage(str("TIR " + str(i) + " " + str(Ressources.LTirX[i]) + " " + str(Ressources.LTirY[i]) + " ///")) 
	
	def EnvoiVie(self, numeroJoueur): #Envoi la vie du joueur a tous les joueurs
		Envoi.EnvoyerMessage(str("VIE 0 0 " + str(Ressources.LVie[numeroJoueur]) + " ///"), numeroJoueur)
		if Ressources.LVie[numeroJoueur] <= 0: #Si le joueur est mort on lui redonne des points de vie (on est gentil quand meme)
			Ressources.LVie[numeroJoueur] = int(4)
						
"""A faire:
1.Integrer la collision avec le personnage (voir client)
2.Coder la fonction qui supprime la balle dans la table (doit synchro avec les threads)
3.Identifier l'appartenance de la balle de chaque joueur 
4. Fonction qui tue le personnage et ajoute le point au joueur (remettre au spawn ?)"""