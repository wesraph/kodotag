"""
Thread unique a chacun des  joueurs qui receptionne
les commandes envoyees par le joueur a 
qui elle est associee et appelle les bonnes
fonctions utiles a leur traitement
"""

import Ressources
import Reseau

def Reception(numeroJoueur):
	print "Creation de la thread Reception n" , numeroJoueur
	
	
	while Ressources.EnJeu == 1:
	
		Recu = "0" 
		while (("///" in Recu) != 1):
			Recu += Ressources.Lsocket[numeroJoueur].recv(1)
		Recu.decode()
		#On separe les donnes envoyees
		(Commande, VariableA, VariableB, SertARien) = Recu.split()
		
		#On traite
		if("POS1" in Commande): #Change la position du joueur
			Ressources.LPositionX[numeroJoueur] = VariableA
			Ressources.LPositionY[numeroJoueur] = VariableB
		if("POS2" in Commande):
			Ressources.LOrientation[numeroJoueur] = VariableA
			Ressources.LMouvement[numeroJoueur] = VariableB
		if("TIR" in Commande): #On recoit que le joueur a tire
			Tirer(int(VariableA), numeroJoueur)


def AAjouter(numeroJoueur): #Cherche si dans le tableau de balles on a une balle supprimee auparavant 
	i = 0
	while(i < len(Ressources.LTirX)):
		if (Ressources.LTirX[i] == 0 and Ressources.LTirY[i] == 0):
			return i
		else:
			i+=1
	return i
def ReceptionPseudo(numeroJoueur):#Receptionne le pseudo du joueur
	Pseudo = "" #On doit creer la variable avant la boucle
	while(("///" in Pseudo) != 1):
		Pseudo = Pseudo + str(Ressources.Lsocket[numeroJoueur].recv(1))
	Ressources.LPseudo.append(Pseudo[:-3])
	
def Tirer(VariableC, numeroJoueur):
	Ressources.EnChangement = 1
	#On ajoute la position du joueur comme point initial du tir
	i = AAjouter(numeroJoueur) #Notre compteur
	if(i < len(Ressources.LTirX)): #Si on a un emplacement libre
	
		#Place la balle a la position du joueur
		Ressources.LTirX[i] = Ressources.LPositionX[numeroJoueur]
		Ressources.LTirY[i] = Ressources.LPositionY[numeroJoueur]
		Ressources.LTireur[i] = numeroJoueur
		
		#Affecte la vitesse a la balle selon l'orientation du tir
		if(VariableC == 2): #Sens vers la gauche
			Ressources.LAccX[i] = -Ressources.VitesseBalle
			Ressources.LAccY[i] = 0
		if(VariableC == 3): #Sens vers la droite
			Ressources.LAccX[i] = Ressources.VitesseBalle
			Ressources.LAccY[i] = 0
		if(VariableC == 0): #Sens vers le haut
			Ressources.LAccX[i] = 0
			Ressources.LAccY[i] = -Ressources.VitesseBalle
		if(VariableC == 1): #Sens vers le bas
			Ressources.LAccX[i] = 0
			Ressources.LAccY[i] = Ressources.VitesseBalle
			
	else: #Si aucun emplacement est libre, on en creait un 
	
		Ressources.LTirX.append(Ressources.LPositionX[numeroJoueur])
		Ressources.LTirY.append(Ressources.LPositionY[numeroJoueur])
		Ressources.LTireur.append(numeroJoueur)
		
		if(VariableC == 2):#Sens vers la gauche
			Ressources.LAccX.append(-Ressources.VitesseBalle)
			Ressources.LAccY.append(0)
		if(VariableC == 3):#Sens vers la droite
			Ressources.LAccX.append(Ressources.VitesseBalle)
			Ressources.LAccY.append(0)
		if(VariableC == 0):#Sens vers le haut
			Ressources.LAccX.append(0)
			Ressources.LAccY.append(-Ressources.VitesseBalle)
		if(VariableC == 1):#Sens vers le bas
			Ressources.LAccX.append(0)
			Ressources.LAccY.append(Ressources.VitesseBalle)
		
	Ressources.EnChangement = 0