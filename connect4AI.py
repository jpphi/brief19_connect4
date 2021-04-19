# Plateau
#from  import Alea
import numpy as np
import pygame
import sys
import os

"""
from keras.models import load_model
import random
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

from collections import deque

"""



sys.path.append("./classes")
#sys.path.insert(0,"./classes") ####### A TESTER
#sys.path.append("classes") ####### A TESTER
from plateau import *
from joueur import *
from entsort import *
from game import *
from DQN import *

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')



game= Game(play1= "CodeR43", play2= "CodeR43", inout= "console", board= (6,7,4), training_mode= 50, tournement_mode= 0, \
    modelplay1= "./modeles/m24-42-7/model 257-CODER43 vs CODER43 102 91.h5", modelplay2="")

if game.training_mode(): game.apprentissage()
if game.tournement_mode(): game.tournoi()

