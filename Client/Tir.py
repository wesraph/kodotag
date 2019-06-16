"""
Envoi les bons messages selon le tir
"""

import Reseau
import res
NombreDeTirsMax = 10
LPositionX = list()
LPositionY = list()

def TirHaut():
	if(res.RenduMultijoueurs == 1): #On traite la partie plus basse que si on est connecte et que la partie est en cours
		Reseau.EnvoyerMessage(str("TIR " + "0" + " " +  "0" + " ///")) #On envoi au serveur qu'on vient de tirer vers le haut	
def TirBas():
	if(res.RenduMultijoueurs == 1): #On traite la partie plus basse que si on est connecte et que la partie est en cours
		Reseau.EnvoyerMessage(str("TIR " + "1" + " " +  "0" + " ///")) #On envoi au serveur qu'on vient de tirer vers le haut	
def TirGauche():
	if(res.RenduMultijoueurs == 1): #On traite la partie plus basse que si on est connecte et que la partie est en cours
		Reseau.EnvoyerMessage(str("TIR " + "2" + " " +  "0" + " ///")) #On envoi au serveur qu'on vient de tirer vers le haut	
def TirDroite():
	if(res.RenduMultijoueurs == 1): #On traite la partie plus basse que si on est connecte et que la partie est en cours
		Reseau.EnvoyerMessage(str("TIR " + "3" + " " +  "0" + " ///")) #On envoi au serveur qu'on vient de tirer vers le haut	
