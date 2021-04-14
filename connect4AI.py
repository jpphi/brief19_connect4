# Plateau
import numpy as np
import pygame
import sys
import os
import time

#import unittest

sys.path.append("./classes")
#sys.path.insert(0,"./classes") ####### A TESTER
#sys.path.append("classes") ####### A TESTER
from plateau import *
from joueur import *
from entsort import *

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

def joue(joueur, jeu, es):
    # Joueur 1  FAIRE UNE FCT AVEC JEU ET JOUEUR EN PARAMETRE
    if joueur.get_type()== "HUMAIN":
        colonne= es.entre_cp(jeu.ColonneDispo(),  message= f"{joueur.nom} 1, colonne ?: ")
    elif joueur.get_type()== "BOT":
        colonne= joueur.bot_joue(jeu.ColonneDispo())

    matrice, fin_de_jeu, recompense= jeu.place_jeton(colonne,joueur.get_couleur())
    es.aff_matrice(jeu.get_board())


    return matrice, fin_de_jeu, recompense
"""     
    if fin_de_jeu:
        joueur.recompense(recompense)
        joueur2.recompense(-recompense)
        break

    if jeu.plein(): break ## Affichage d'un message sur le plateau de jeu
"""
    

# Construction d'un tableau:
jeu= Plateau(largeur= 7, hauteur= 6, a_la_suite= 4)
jeu.init_board()

# Choix des joueurs
joueur1= Humain(couleur= 1)
joueur2= Alea(couleur= -1)

# Choix des entrées / sorties
#es= Console()
es= py_game()

#es.aff_matrice(jeu.get_board())


if es.get_type_entsort()== "pygame": # IMPOSER UN PLATEAU 7x6
    pass

es.aff_matrice(jeu.get_board())
while True:

    matrice, fin_de_jeu, recompense= joue(joueur1, jeu, es)

    """
    # Joueur 1  FAIRE UNE FCT AVEC JEU ET JOUEUR EN PARAMETRE
    if joueur1.get_type()== "HUMAIN":
        colonne= es.entre_cp(jeu.ColonneDispo(),  message= f"{joueur1.nom} 1, colonne ?: ")
    elif joueur1.get_type()== "BOT":
        colonne= joueur1.bot_joue(jeu.ColonneDispo())

    matrice, fin_de_jeu, recompense= jeu.place_jeton(colonne,joueur1.get_couleur())
    es.aff_matrice(jeu.get_board())
    """

    if fin_de_jeu:
        joueur1.recompense(recompense)
        joueur2.recompense(-recompense)
        break

    if jeu.plein(): break ## Affichage d'un message sur le plateau de jeu

    matrice, fin_de_jeu, recompense= joue(joueur2, jeu, es)

    """
    # Joueur 2
    if joueur2.get_type()== "HUMAIN":
        colonne= es.entre_cp(jeu.ColonneDispo(),  message= f"{joueur2.nom} 2, colonne ?:")
    elif joueur2.get_type()== "BOT":
        colonne= joueur2.bot_joue(jeu.ColonneDispo())

    matrice, fin_de_jeu, recompense= jeu.place_jeton(colonne,joueur2.get_couleur())
    es.aff_matrice(jeu.get_board())
    """
    if fin_de_jeu:
        joueur1.recompense(-recompense)
        joueur2.recompense(recompense)
        break

    if jeu.plein(): break ## Affichage d'un message sur le plateau de jeu


print(f"Récompence joueur 1: {joueur1.get_recompense()}")
print(f"Récompence joueur 2: {joueur2.get_recompense()}")

es.aff_matrice(jeu.get_board())

input(f"Fin de partie: entrez pour quitter !")
