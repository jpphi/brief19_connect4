import numpy as np
import pygame
import sys
import os


import argparse

sys.path.append("./classes")
#sys.path.insert(0,"./classes") ####### A TESTER
#sys.path.append("classes") ####### A TESTER
from plateau import *
from joueur import *
from entsort import *
from game import *
from DQN import *



# Ligne de commande, utilisation de argparse
parser = argparse.ArgumentParser(description='Power 4 !')
parser = argparse.ArgumentParser()
parser.version = '1.0'

#---------------------
#parser.add_argument('--reg-rate', type=float, dest='reg_rate', default=0.01) # Essayer dest pour alléger le code

parser.add_argument('--play1','-p1', action='store', help='--play1 "Humain" or "CodeR4" or "CodeR43" or "Jedi" or nothing (=Humain)')
parser.add_argument('--play2','-p2', action='store', help='--play2 "Humain" or "CodeR4" or "CodeR43" or "Jedi" or nothing (=Humain)')

parser.add_argument('--inout','-io', action='store', help='--inout "console" or "pygame" or "tkinter" or nothing (=console)')

parser.add_argument('--board','-b', action='store', type= int, help='--board integer integer integer', nargs= 3)

parser.add_argument('--training_mode','-trm', action='store', type= int, help='--training_mode integer')
parser.add_argument('--tournement_mode','-tm', action='store', type= int,  help='--tournement_mode integer')

parser.add_argument('--modelplay1','-mp1', action='store', help='--modelplay1 path/file.h5')
parser.add_argument('--modelplay2','-mp2', action='store', help='--modelplay2 path/file.h5')
parser.add_argument('--loadmodel','-lm', action='store', help='--loadmodel path/file.h5')

parser.add_argument('--num_model1','-nm1', action='store', help='--num_model1 N N est le numéro du modèle du reseau de neurone utilisé')
parser.add_argument('--num_model2','-nm2', action='store', help='--num_model2 N N est le numéro du modèle du reseau de neurone utilisé')
parser.add_argument('--num_model','-nm', action='store', help='--num_model N N est le numéro du modèle du reseau de neurone utilisé')

"""
python connect4.py --help
python connect4.py --mode hxh  # pour humain contre humain
python connect4.py --mode hxr  # pour humain contre robot (humain commencent)
python connect4.py --mode rxh  # pour humain contre robot (robot commence)
python connect4.py --mode rxr  # pour robot contre robot
"""
# parser.add_argument('-c', action='store_true')
# parser.add_argument('-e', action='append')
# parser.add_argument('-f', action='append_const', const=42)
# parser.add_argument('-g', action='count')
# parser.add_argument('-j', action='version')

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

#----------------------------------------- Ligne de commande complète ---------------------------------------------------------------
# python connect4AI.py -p1 "Jedi" -p2 "CodeR43" -io "console" -b 6 7 4 -trm 200 -tm 0 -mp1 "./model-20_100_150_100_50_20_1_m-col 100-JEDI43 vs CODER43 0 100 0.h5" -mp2 "./modeles/M20-100-100-1/model-20-100-100-1 200-CODER43 vs CODER43 79 79 42.h5" -nm1 1 -nm2 1
#------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    arguments = parser.parse_args()
    #print("arguement",arguments)    

 
    if arguments.play1 not in ["Humain","CodeR4","CodeR43","Jedi","Alea"]:
         arguments.play1= "Humain"
    if arguments.play2 not in ["Humain","CodeR4","CodeR43","Jedi","Alea"]:
         arguments.play2= "Humain"

    if arguments.inout not in ["console","pygame","tkinter"]:
        arguments.inout= "console"

    if arguments.board== None: arguments.board= (6,7,4) ##########################################

    if arguments.training_mode== None: arguments.training_mode= 0
    if arguments.tournement_mode== None: arguments.tournement_mode= 1

    if arguments.num_model1== None: arguments.num_model1= 1
    if arguments.num_model2== None: arguments.num_model2= 1
    if arguments.num_model== None: arguments.num_model= 1

    #------------------------- A FAIRE --------------------------------------
    #
    # FAIRE UNE METHODE ENREGISTREMENT PARTIE Pour utiliser les partie h/h en apprentissage ensuite
    # + methode rejouer partie
    # Integrer tkinter
    # faire des docstring
    # Bug chargement jedi en reseau convolutionnel
    # Utiliser act qui donnerai un peu d aleatoire dans le comportement de jedi
    #
    #------------------------------------------------------------------------
    
    # POUR LANCER EN LIGNE DE COMMANDE, DÉCOMMENTER CETTE LIGNE ET COMMENTER LA SUIVANTE
    """
    game= Game(play1=  arguments.play1, play2= arguments.play2, inout= arguments.inout, board= (6,7,4),\
                training_mode= arguments.training_mode, tournement_mode= arguments.tournement_mode, \
                modelplay1= arguments.modelplay1, modelplay2= arguments.modelplay2,\
                num_model1= arguments.num_model1, num_model2= arguments.num_model2,\
                num_model= arguments.num_model)
    """
    game= Game(play1= "Jedi", play2= "Jedi", inout= "pygame", board= (6,7,4), \
                training_mode= 0, tournement_mode= 100, \
                modelplay1= "model-type1 et 1 200-JEDI vs JEDI 200 0 0.h5", \
                modelplay2="model-type2 et 2 450-JEDI vs CODER 2 448 0.h5",\
                loadmodel= "model-type2 et 2 450-JEDI vs CODER 2 448 0.h5",\
                num_model= 2, num_model1= 1, num_model2= 2, param= {"tau":1, "epsilon":2})

    if game.training_mode(): game.apprentissage()
    if game.tournement_mode(): game.tournoi()
