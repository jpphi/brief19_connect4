# Plateau
#from  import Alea
import numpy as np
import pygame
import sys
import os
import time

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



game= Game(play1= "Jedi", play2= "CodeR4", inout= "console", board= (6,7,4), training_mode= 5, tournement_mode= 0, \
    modelplay1= "./model420-210-84-7 250-ROGER - vs ROGER j1 123 - j2 119 n 8.h5")

if game.training_mode(): game.apprentissage()
if game.tournement_mode(): game.tournoi()

