# Plateau
import numpy as np
import pygame
import sys
import os

sys.path.append("./classes")
#sys.path.insert(0,"./classes") ####### A TESTER
#sys.path.append("classes") ####### A TESTER
from plateau import *
from joueur import *
from entsort import *

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


    

# Construction d'un tableau:
jeu= Plateau(largeur= 7, hauteur= 6, a_la_suite= 4)
jeu.init_board()

# Choix des joueurs
joueur1= Humain(couleur= 1)
joueur2= Humain(couleur= 2)

# Choix des entrées / sorties
#es= Console()
es= py_game()

#es.aff_matrice(jeu.get_board())

#import unittest

if es.get_type_entsort()== "pygame": # IMPOSER UN PLATEAU 7x6
    pass

es.aff_matrice(jeu.get_board())
while True:

    # Joueur 1  FAIRE UNE FCT AVEC JEU ET JOUEUR EN PARAMETRE
    colonne= es.entre_cp(jeu.ColonneDispo(),  message= "joueur1")
    matrice, fin_de_jeu, recompense= jeu.place_jeton(colonne,joueur1.get_couleur())
    es.aff_matrice(jeu.get_board())

    if fin_de_jeu:
        joueur1.recompense(recompense)
        joueur2.recompense(-recompense)
        break

    if jeu.plein(): break ## Affichage d'un message sur le plateau de jeu

    # Joueur 2
    colonne= es.entre_cp(jeu.ColonneDispo(),  message= "Colonne ?:")
    matrice, fin_de_jeu, recompense= jeu.place_jeton(colonne,joueur2.get_couleur())
    es.aff_matrice(jeu.get_board())

    if fin_de_jeu:
        joueur1.recompense(-recompense)
        joueur2.recompense(recompense)
        break

    if jeu.plein(): break ## Affichage d'un message sur le plateau de jeu


print(f"Récompence joueur 1: {joueur1.get_recompense()}")
print(f"Récompence joueur 2: {joueur2.get_recompense()}")
