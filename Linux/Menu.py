import sys, os
import pygame, pygame.font, pygame.event, pygame.draw, string
import KodoTrueVersion, res, Sprites
from pygame.locals import *
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
	
# On definit une largeur et une hauteur	dans une variable size
size = width, height = 640, 480
# On initialise Pygame
pygame.init()

# On definit un nom pour la fenetre
fenetre = pygame.display.set_caption("Super Mortal Combat Fight")
# On definit la taille de la fenetre avec la variable size
fenetre = pygame.display.set_mode((size))

#--------------On definit les images puis on les collent en suivant un ordre particulier (images de derriere puis celles de devant)------------------#
fond = pygame.image.load("images/supermortal.jpg").convert()
fenetre.blit(fond, (0,0))
fondtrans = pygame.image.load("images/fondtrans.jpg").convert()
fenetre.blit(fondtrans, (5,65))
jouer = pygame.image.load("images/connect.jpg").convert()
fenetre.blit(jouer, (11,70))
para = pygame.image.load("images/option.jpg").convert()
fenetre.blit(para, (11,151))
aide = pygame.image.load("images/aide.jpg").convert()
fenetre.blit(aide, (11,232))
credit = pygame.image.load("images/credit.jpg").convert()
fenetre.blit(credit, (11,313))
quitter = pygame.image.load("images/quitter.jpg").convert()
fenetre.blit(quitter, (11,394))

# On utilise le module mixer pour ajouter une musique d'arriere plan
pygame.mixer.music.load("Musiques/Epic Battle Music.mp3")
pygame.mixer.music.play()

# On reactualise la fenetre
pygame.display.flip()

#  On definit les variables
continuer = 1 
continuer_accueil = 1
continuer_lancement = 0
continuer_parametres = 0
sound = 1
screen = 1
Sprites.NumeroPersonnage = 0

#DEFINITION DE TOUTES LES FONCTIONS D'AFFICHAGE DES BOUTONS#
def menu_principal(): # Affichage du menu principal
	fond = pygame.image.load("images/supermortal.jpg").convert()
	fenetre.blit(fond, (0,0))
	fondtrans = pygame.image.load("images/fondtrans.jpg").convert()
	fenetre.blit(fondtrans, (5,65))
	jouer = pygame.image.load("images/connect.jpg").convert()
	fenetre.blit(jouer, (11,70))
	para = pygame.image.load("images/option.jpg").convert()
	fenetre.blit(para, (11,151))
	aide = pygame.image.load("images/aide.jpg").convert()
	fenetre.blit(aide, (11,232))
	credit = pygame.image.load("images/credit.jpg").convert()
	fenetre.blit(credit, (11,313))
	quitter = pygame.image.load("images/quitter.jpg").convert()
	fenetre.blit(quitter, (11,394))
	pygame.display.flip
def menu_lancement(): # Affichage du menu de connexion
	font = pygame.font.Font(None, 15)
	text = font.render("Pseudo :", 1, (255, 255, 255))
	text1 = font.render("Adresse :", 1,(255, 255, 255))
	fondtrans = pygame.image.load("images/fondtrans.jpg").convert()
	fenetre.blit(fondtrans, (5,65))
	retour = pygame.image.load("images/retour.jpg").convert()
	fenetre.blit(retour, (11,394))
	skin = pygame.image.load("images/skin.jpg").convert()
	fenetre.blit(skin, (11,151))
	lancer = pygame.image.load("images/lancer.jpg").convert()
	fenetre.blit(lancer, (11,313))
	adresse()
	pseudo()
	fenetre.blit(text, (55,125))
	fenetre.blit(text1, (55,260))
	pygame.display.flip()
def menu_options(): # Affichage du menu de parametres
	font = pygame.font.Font(None, 15)
	text = font.render("Adresse :", 1, (255, 255, 255))
	text = font.render("Port :", 1, (255, 255, 255))
	resolution = pygame.image.load("images/resolution.jpg").convert()
	fenetre.blit(resolution, (11,70))
	fullscreen = pygame.image.load("images/pleinecran.jpg").convert()
	fenetre.blit(fullscreen, (11,151))
	son = pygame.image.load("images/musique.jpg").convert()
	fenetre.blit(son, (11,232))
	retour = pygame.image.load("images/retour.jpg").convert()
	fenetre.blit(retour, (11,394))
	fenetre.blit(text, (55,341))
	pygame.display.flip()
def aide(): # Affichage de l'aide
	aide1 = pygame.image.load("images/aide1.jpg").convert()
	fenetre.blit(aide1, (170,65))
	pygame.display.flip()
def credit(): # Affichage des credits
	credit1 = pygame.image.load("images/credit1.jpg").convert()
	fenetre.blit(credit1, (170,65))
	pygame.display.flip()
def choix_skin(): # Affichage du menu de choix de skin
	ok = pygame.image.load("images/ok.jpg").convert()
	fenetre.blit(ok,(220,165))
	next = pygame.image.load("images/next.jpg").convert()
	fenetre.blit(next,(270,115))
	pygame.display.flip()
def affichage_skin():  # Fonction permettant le changement de skin
	if Sprites.NumeroPersonnage == 0:
		s = pygame.image.load("images/0.png").convert_alpha()
		fenetre.blit(s, (220,65))
		pygame.display.flip()
	elif Sprites.NumeroPersonnage == 1:
		s = pygame.image.load("images/1.png").convert_alpha()
		fenetre.blit(s, (220,65))
		pygame.display.flip()
	elif Sprites.NumeroPersonnage == 2:
		s = pygame.image.load("images/2.png").convert_alpha()
		fenetre.blit(s, (220,65))
		pygame.display.flip()
	pygame.display.flip
def pseudo():  # Affichage de la boite de dialogue Pseudo
	fontobject = pygame.font.Font(None, 15) # On definit un objet de type texte avec sa police, (ici "None" veut dire police par defaut), et sa taille
	pygame.draw.rect(fenetre, (0,0,0), (12,71, 147,69), 0) # On dessine un rectangle noir qui est rempli
	pygame.draw.rect(fenetre, (206,206,206), (11,70, 148,70), 1) # On dessine un second rectangle blanc qui encadre le premier
	pygame.display.flip()
def adresse(): # Affichage de la boite de dialogue Adresse serveur
	fontobject = pygame.font.Font(None, 15)
	pygame.draw.rect(fenetre, (0,0,0), (12,232, 147,69), 0)
	pygame.draw.rect(fenetre, (206,206,206), (11,231, 148,70), 1)
	pygame.display.flip()
def port():    # Affichage de la boite de dialogue Port
	fontobject = pygame.font.Font(None, 15)
	pygame.draw.rect(fenetre, (0,0,0), (12,313, 147,69), 0)
	pygame.draw.rect(fenetre, (206,206,206), (11,312, 148,70), 1)
	pygame.display.flip()
	
#--------------------------DEFINITION DE TOUTES LES FONCTIONS LIEES AUX BOITE DE DIALOGUES----------------------------------#
def get_key():  # Fonction qui detecte les touches qui sont appuyees
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass
def ask(fenetre, question):  # Fonction qui place les touches appuyees dans une chaine de caracteres
  pygame.font.init()
  current_string = [] # Chaine de carateres ou le texte qui est tape est mis
  display_box(fenetre, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key() # On appelle la fonction get_key() qui gere les evenements au clavier
    if inkey == K_BACKSPACE:  # Si on appuie sur "Retour" on efface la derniere lettre de la chaine de caracteres
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break # Si on appuie sur entrer, on sort de la boucle
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(fenetre, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")
def ask1(fenetre, question):
  pygame.font.init()
  current_string = []
  display_box1(fenetre, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box1(fenetre, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")
def ask2(fenetre, question):
  pygame.font.init()
  current_string = []
  display_box2(fenetre, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key() 
    if inkey == K_BACKSPACE:  
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break 
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box2(fenetre, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")
def display_box(screen, message): # On cree une boite de dialogue
	fontobject = pygame.font.Font(None, 15) # On definit la police, la taille du texte
	pygame.draw.rect(fenetre, (0,0,0), (12,71, 147,69), 0) # On cree un rectangle noir rempli
	pygame.draw.rect(fenetre, (206,206,206), (11,70, 148,70), 1) # On cree un rectangle blanc qui entoure le premier
	if len(message) != 0:
		fenetre.blit(fontobject.render(message, 1, (255,255,255)), (55,125)) # On affiche le texte ecrit dans la boite de dialogue
	pygame.display.flip()
def display_box1(screen, message):
	fontobject = pygame.font.Font(None, 15)
	pygame.draw.rect(fenetre, (0,0,0), (12,232, 147,69), 0)
	pygame.draw.rect(fenetre, (206,206,206), (11,231, 148,70), 1)
	if len(message) != 0:
		fenetre.blit(fontobject.render(message, 1, (255,255,255)), (55,260))
	pygame.display.flip()
def display_box2(screen, message): 
	fontobject = pygame.font.Font(None, 15)
	pygame.draw.rect(fenetre, (0,0,0), (12,313, 147,69), 0)
	pygame.draw.rect(fenetre, (206,206,206), (11,312, 148,70), 1)
	if len(message) != 0:
		fenetre.blit(fontobject.render(message, 1, (255,255,255)), (55,340))
	pygame.display.flip()


#--------------Boucle Principale------------------#
	
while continuer:
	if sound%2 == 0:       # On verifie si la musique a ete coupe, si oui la musique est arrete, si non elle continue
		pygame.mixer.music.pause()
	else: pygame.mixer.music.unpause()
	while continuer_accueil:   # On entre dans la boucle du menu d'accueil
		menu_principal() # Appel de la fonction menu_principal ( Affichage des boutons)
		for event in pygame.event.get():    # Gestion des evenements
			if event.type == QUIT:      # Evenement de fermetures : Touche Echap ou Fermer avec la "croix rouge"
				continuer_accueil = 0    # On quitte le menu d'accueil ainsi que la boucle principale, le programme se ferme
				continuer = 0 
			if event.type == MOUSEBUTTONDOWN:  # Si il y a un evenement de type clique 
				if event.button == 1:   # Si c'est un clique gauche
					if 11 < event.pos[0] < 159 and 394< event.pos[1] < 464:  # On definit la zone de clique en abscisse puis en ordonnee
						continuer_accueil = 0      # Clique sur quitter, le programme se ferme
						continuer = 0
					elif 11 < event.pos[0] < 159 and 70 < event.pos[1] < 140:  # Clique sur le bouton de connexion on entre dans la boucle continuer_lancement
						continuer_accueil = 0
						continuer_lancement = 1
					elif 11 < event.pos[0] < 159 and 151 < event.pos[1] < 221: # Clique sur le bouton d'options on entre dans la boucle continuer_parametres
						continuer_accueil = 0
						continuer_parametres = 1	
					elif 11 < event.pos[0] < 159 and 232 < event.pos[1] < 302: # Affichage des regles et de l'aide
						aide()
					elif 11 < event.pos[0] < 159 and 313 < event.pos[1] < 383: # Affichage des credits
						credit()
	while continuer_lancement: # Boucle menu connexion
		menu_lancement()
		for event in pygame.event.get():
			if event.type == QUIT:    
				continuer_parametres = 0
				continuer = 0 
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 11 < event.pos[0] < 159 and 394< event.pos[1] < 464:   # Clique sur le bouton retour, on revient au menu principal
						continuer_lancement = 0
						continuer_accueil = 1
						menu_principal()	
					elif 11 < event.pos[0] < 159 and 70 < event.pos[1] < 140: # On entre le Pseudo dans une boite de dialogue
						print "Pseudo :" + ask(screen, "Pseudo") 
					elif 11 < event.pos[0] < 159 and 232 < event.pos[1] < 302:
						print "Adresse serveur:" + ask1(screen, "Adresse") # On entre l'adresse du serveur dans une boite de dialogue
					elif 11 < event.pos[0] < 159 and 151 < event.pos[1] < 221: # Changement de skin du personnage
						choix_skin()
						affichage_skin()
						pygame.display.flip
					elif 220 < event.pos[0] < 270 and 165< event.pos[1] < 215:
						print  ("Choix de skin:" + str(Sprites.NumeroPersonnage))
						pygame.display.flip
					elif 270 < event.pos[0] < 320 and 115< event.pos[1] < 165:	
						Sprites.NumeroPersonnage += 1
						affichage_skin()
						if Sprites.NumeroPersonnage == 3:
							Sprites.NumeroPersonnage = 0
							affichage_skin()
						pygame.display.flip
					elif 11 < event.pos[0] < 159 and 313 < event.pos[1] < 383:
						KodoTrueVersion.lancement() # On lance le client du jeu (il faut au prealable lancer le serveur)
			pygame.display.flip()
	while continuer_parametres: # Boucle options, parametres
		menu_options()
		port()
		for event in pygame.event.get():
			if event.type == QUIT:    
				continuer_parametres = 0
				continuer = 0 
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 11 < event.pos[0] < 159 and 70 < event.pos[1] < 140: # Menu pour changer la resolution de la fenetre ( Non implemente )
						print("Choix de la resolution de l'ecran non implemente")
					if 11 < event.pos[0] < 159 and 151 < event.pos[1] < 221:  # Passage en mode Plein-ecran ou retour en mode fenetre
						screen += 1
						if screen%2 == 0:
							fenetre = pygame.display.set_mode((size),FULLSCREEN)
							menu_principal()
						else: fenetre = pygame.display.set_mode((size)) and menu_principal()
						pygame.display.flip()
					if 11 < event.pos[0] < 159 and 232 < event.pos[1] < 302:  # On stoppe la musique ou on la relance
						sound += 1
						if sound%2 == 0:
							pygame.mixer.music.pause()
						else: pygame.mixer.music.unpause()
					if 11 < event.pos[0] < 159 and 394 < event.pos[1] < 464: 
						continuer_parametres = 0
						continuer_accueil = 1
						menu_principal()
					if 11 < event.pos[0] < 159 and 313 < event.pos[1] < 383: # On entre le Port dans une boite de dialogue
						print "Port:" + ask2(screen, "Port")
		pygame.display.flip()
	pygame.display.flip()	
pygame.display.flip()