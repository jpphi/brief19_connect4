
import numpy as np
import pygame

class Plateau:
    # Attribut de classe: private
    __compteur_plateau= 0
    __LARGEUR= 7
    __HAUTEUR= 6
    __A_LA_SUITE= 4
    
    __MINIMUM_LARGEUR= __A_LA_SUITE
    __MINIMUM_HAUTEUR= __A_LA_SUITE
    
    # JOUEUR OU PLATEAU VISU?
    _ROUGE= 2
    _NOIR= 1
    _VIDE= 0

    __board=[] # Anciennement mat
    __MAT_ID=[]
    __MAT_COL=[]
    
    __CONTINUE= 1
    __STOP= 0
    __RECOMPENSE= 0

    
    
    def __init__(self, largeur= __LARGEUR, hauteur= __HAUTEUR, a_la_suite= __A_LA_SUITE ):
        print(largeur, hauteur, a_la_suite)
        if largeur < Plateau.__MINIMUM_LARGEUR or hauteur < Plateau.__MINIMUM_HAUTEUR or a_la_suite < 3 or \
            a_la_suite >  min(largeur, hauteur):
            msg= f"La dimension minimum de la matrice doit être de {Plateau.__MINIMUM_LARGEUR} x {Plateau.__MINIMUM_HAUTEUR}.\n"+\
                   f"D'autre par le nombre d'alignement (ici {a_la_suite}) doit être supérieur à 3 et inférieur à {min(largeur, hauteur)}"
            raise ValueError(msg)
        self.__compteur_plateau+= 1
        self.__LARGEUR= largeur
        self.__HAUTEUR= hauteur
        self.__board= np.zeros((hauteur,largeur), dtype= int)
        self.__MAT_ID= np.eye(a_la_suite,dtype= int)
        self.__MAT_COL_1= np.ones((a_la_suite,1), dtype= int)
        
    def affiche_param(self):
        print(f"Compteur: {self.__compteur_plateau}")
        print(f"Largeur: {self.__LARGEUR}")
        print(f"Hauteur: {self.__HAUTEUR}")
        print(f"Puissance: {self.__A_LA_SUITE}")
        print(f"État du plateau:\n{self.__board}")
        print(f"\nMatrice ID:\n{self.__MAT_ID}")
        print(f"\nMatrice Col_1:\n{self.__MAT_COL_1}")
        
        
    def plein(self):
        m= 1
        for i in range(self.__LARGEUR):
            m*= self.__board[0][i]
            if m== 0: return False
        return True
    
    def get_board(self):
        return self.__board
    
    def ColonneDispo(self):
        cd=[]
        for i in range(self.__LARGEUR):
            if self.__board[0][i]== 0: cd.append(i+1)
        return cd
    
    def place_jeton(self, col, couleur):
        fenetre= np.array(self.__A_LA_SUITE * [couleur])
        recompense= 0
        fin_de_jeu= 0
        
        col= col- 1 # On joue à partir de la colonne 1 qui correspond à la colonne 0 du __board
        colonne= self.__board[:,col].reshape(self.__board.shape[0]) # on récupère la colonne 'col' de la matrice board
        a= np.where(colonne== 0)
        lig= a[0].max()
        self.__board[lig,col]= couleur
        
        # FAIRE UNE METHODE DE CLASSE VICTOIRE
        
        colonne = self.__board[lig:lig+self.__A_LA_SUITE,col]
        if len(colonne) >= self.__A_LA_SUITE:
            gagne= self.__verif_colonne(colonne, fenetre)
            if gagne:
                recompense= 1
                fin_de_jeu= 1
            #print(f"gagne: {gagne} colonne: {colonne} fenetre: {fenetre} fin_de_jeu:{fin_de_jeu}")

        
        return self.__board, fin_de_jeu, recompense
    
    @classmethod
    def __verif_colonne(cls, colonne, fenetre):
        print(f"colonne: {colonne}\nfenetre: {fenetre}")
        print(f"type colonne: {type(colonne)}\ntype fenetre: {type(fenetre)}")
        if np.all([colonne, fenetre]): return True
        return False
        
    def init_board(self):
        self.__board[:,:]= 0
        return self.__board
