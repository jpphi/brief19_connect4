import abc
from abc import ABC, abstractmethod
from random import randint
import numpy as np

class Joueur(ABC):
    _couleur_dispo=[-1,1]

    @abstractmethod
    def nom(self):
        pass

    def get_type(self):
        pass
    

    def get_couleur(self):
        pass

    def recompense(self, gain):
        pass
        
    def get_recompense(self):
        pass

    def get_victoire(self):
        pass

    def inc_victoire(self):
        pass
    
    
class Humain(Joueur):
    __couleur= 0
    __nom= "Humain"
    __recompense= 0
    __TYPE= "HUMAIN"
    
    def __init__(self, couleur= 0, nom= ""):
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            self.__victoire= 0
            #print(self._couleur_dispo)
            
        else:
            print(f"La couleur doit appartenir à la liste {self._couleur_dispo}.")

       
    def nom(self):
        return self.__nom

    def get_type(self):
        return self.__TYPE
    
    def get_couleur(self):
        return self.__couleur
    
    def recompense(self, gain):
        self.__recompense+= gain
        
    def get_recompense(self):
        return self.__recompense

    def get_victoire(self):
        return self.__victoire

    def inc_victoire(self):
        self.__victoire+= 1
        return self.__victoire


class Alea(Joueur):
    __couleur= 0
    __nom= "Alea jacta est"
    __recompense= 0
    __TYPE= "BOT"
    
    def __init__(self, couleur= 0, nom= ""):
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            self.__victoire= 0
            #print(self._couleur_dispo)
            
        else:
            print(f"La couleur doit appartenir à la liste {self._couleur_dispo}.")

       
    def nom(self):
        return self.__nom

    def get_type(self):
        return self.__TYPE
    
    def get_couleur(self):
        return self.__couleur
    
    def recompense(self, gain):
        self.__recompense+= gain
        
    def get_recompense(self):
        return self.__recompense

    def get_victoire(self):
        return self.__victoire

    def inc_victoire(self):
        self.__victoire+= 1
        return self.__victoire
    # Méthode spécifique à la classe bot

    def bot_joue(self,colonne_disponible):
        return colonne_disponible[randint(0,len(colonne_disponible) - 1)]

class Padawan(Joueur):
    __couleur= 0
    __nom= "Anakin"
    __recompense= 0
    __TYPE= "PADAWAN"
    
    def __init__(self, model, couleur= 0, nom= ""):
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            self.__victoire= 0
            print(self._couleur_dispo)
            
        else:
            print(f"La couleur doit appartenir à la liste {self._couleur_dispo}.")

       
    def nom(self):
        return self.__nom

    def get_type(self):
        return self.__TYPE
    
    def get_couleur(self):
        return self.__couleur
    
    def recompense(self, gain):
        self.__recompense+= gain
        
    def get_recompense(self):
        return self.__recompense

    def get_victoire(self):
        return self.__victoire

    def inc_victoire(self):
        self.__victoire+= 1
        return self.__victoire
    # Méthode spécifique à la classe Padawan

    def bot_joue(self,colonne_disponible):
        # recuperer le fichier des poids
        pass

class Jedi(Joueur):
    __couleur= 0
    __nom= "Obiwan"
    __recompense= 0
    __TYPE= "JEDI"
    
    def __init__(self,  model= None, num_model= 0, couleur=0, nom= ""):
        print(f"\n1er ligne de __init__ de Jedi model= {model}\n"+\
            f"num_model={num_model} couleur= {couleur}")
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            self.model= model
            self.num_model= num_model
            self.__victoire= 0
            print(f"\n__init__ de Jedi model= {self.model}\n")
            
        else:
            print(f"La couleur doit appartenir à la liste {self._couleur_dispo}.")

       
    def nom(self):
        return self.__nom

    def get_type(self):
        return self.__TYPE
    
    def get_couleur(self):
        return self.__couleur
    
    def recompense(self, gain):
        self.__recompense+= gain
        
    def get_recompense(self):
        return self.__recompense

    def get_victoire(self):
        return self.__victoire

    def inc_victoire(self):
        self.__victoire+= 1
        return self.__victoire

    # Méthode spécifique à la classe Jedi

    def jedi_joue(self,colonne_disponible, board, jeu, model= None):
        print(f"jedi_joue: model: {model}, num_model: {self.num_model} couleur: {self.__couleur}")
        #cell_dispo= jeu.matrice_cellule_dispo(board)

        b2= np.copy(board)

        if self.num_model== 1:
            b2= b2.reshape(1,board.shape[0] * board.shape[1])
            mat= model.predict(b2)[0]
            #print(f"Jedi_joue aprés reshape, num_model 1. b2.shape: {b2.shape}.\nb2:\n{b2}")
        elif self.num_model== 2:
            b2= b2.reshape(1,board.shape[0],board.shape[1],1)
            #print(f"Jedi_joue avant model.predict, num_model 2. b2.shape: {b2.shape}.\nb2:\n{b2}"+\
            #    f"\nmodel: {model}")
            mat= model.predict(b2)[0]
            print(f"Jedi_joue aprés model.predict, num_model 2. b2.shape: {b2.shape}.\nb2:\n{b2}")
        else:
            raise ValueError("Model non défini !")
        iteration= 0
        while True: # Vérifions que col est disponible avant de retourner sa valeur
            col= (np.argmax(mat))
            mini= mat.min()
            #print(f"Méthode jedijoue apres np.argmax: col= {col}")
            if col+1 not in colonne_disponible:
                mat[col]= mini - 1 # la colonne n'est pas disponible, on l'a "disqualifie"
                #print(f"Dans joueur-jedi_joue. Colonne prédite= {col+1} non disponible !"+\
                #    f" On retire l'élément de {mat}.\nLes colonnes disponible sont: {colonne_disponible}")
                #mat= np.delete(mat,[col])
                #print(f"Aprés retrait: mat= {mat}")
                if iteration> board.shape[1]: # Plus de colonne disponible. Cela ne devrait pas arriver ici!
                    raise ValueError("Dans classe joueur, méthode jedi_joue: Plus de colonne disponible !"\
                        " Ceci ne devrait pas se produire ici car la détection 'plateau plein' se fait en amont.")
                iteration+= 1
            else: break

        print(f"dans jedi joue col: {col}")
        #col = int(input("colonne: "))

        return col + 1

    def get_model(self):
        return self.model

    def get_num_model(self):
        return self.num_model


class CodeR(Joueur):
    __couleur= 0
    __nom= "Attaque_défence"
    __recompense= 0
    __TYPE= "CODER"

    def __init__(self, couleur=0, nom= "", niveau= 4):
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            self.__niveau= niveau
            self.__victoire= 0
            print(f"Dans __init__ niveau= {self.__niveau}")
            
        else:
            print(f"La couleur doit appartenir à la liste {self._couleur_dispo}.")



    def nom(self):
        return self.__nom

    def get_type(self):
        return self.__TYPE
    
    def get_couleur(self):
        return self.__couleur
    
    def recompense(self, gain):
        self.__recompense+= gain
        
    def get_recompense(self):
        return self.__recompense

    def get_victoire(self):
        return self.__victoire

    def inc_victoire(self):
        self.__victoire+= 1
        return self.__victoire

    # Méthode spécifique à la classe bot

    def bot_joue(self,colonne_disponible):
        return colonne_disponible[randint(0,len(colonne_disponible) - 1)]
        #return colonne_disponible[len(colonne_disponible)//2 - 1] # si on ne sais pas quoi jouer, on joue le milieu




    def attaque_defense(self, colonne_disponible, board, a_la_suite):

        print("\nNiveau joueur: ", self.__niveau)

        fenetre= np.array(a_la_suite * [self.__couleur])
        #print(f"fenetre : {fenetre}, colonne_disponible: {colonne_disponible} ala_suite: {a_la_suite}")
        #print(f"board : {board}")

        for col in colonne_disponible:
            col= col- 1 # On joue à partir de la colonne 1 qui correspond à la colonne 0 du __board
            gagne= self.jeu_fictif(board, a_la_suite, col, fenetre)

            if gagne!= -1:
                return gagne # gagne contient la colonne à jouer qui permet de gagner

        # Toutes les colonnes ont été essayer, pas de possibilité de gagner, on teste si l'aversaire peut gagner

        board= -1 * board # On se place du point de vue de l'adversaire
        #fenetre= - 1 * fenetre

        for col in colonne_disponible:
            col= col- 1 # On joue à partir de la colonne 1 qui correspond à la colonne 0 du __board
            gagne= self.jeu_fictif(board, a_la_suite, col, fenetre)

            if gagne!= -1:
                return gagne # gagne contient la colonne à jouer qui permet de gagner


        # Toutes les colonnes ont été essayer, l'aversaire ne peut gagner

        if self.__niveau== 4:
            return self.bot_joue(colonne_disponible) # on s'en remet au hazard
            
        elif self.__niveau== 43: # On cherche à placer 3 pions ou empecher l'adversaire d'en placer 3
            print("\n43\n")
            fenetre= np.array( (a_la_suite-1) * [self.__couleur])
            #print(f"fenetre : {fenetre}, colonne_disponible: {colonne_disponible} ala_suite: {a_la_suite}")
            #print(f"board : {board}")

            for col in colonne_disponible:
                col= col- 1 # On joue à partir de la colonne 1 qui correspond à la colonne 0 du __board
                gagne= self.jeu_fictif(board, a_la_suite, col, fenetre)

                if gagne!= -1:
                    return gagne # gagne contient la colonne à jouer qui permet de gagner

            # Toutes les colonnes ont été essayer, pas de possibilité de gagner, on teste si l'aversaire peut gagner

            board= -1 * board # On se place du point de vue de l'adversaire
            #fenetre= - 1 * fenetre

            for col in colonne_disponible:
                col= col- 1 # On joue à partir de la colonne 1 qui correspond à la colonne 0 du __board
                gagne= self.jeu_fictif(board, a_la_suite, col, fenetre)

                if gagne!= -1:
                    return gagne # gagne contient la colonne à jouer qui permet de gagner


            # Toutes les colonnes ont été essayer, # on s'en remet au hazard
                return self.bot_joue(colonne_disponible) # on s'en remet au hazard





    def jeu_fictif(self, board, a_la_suite, col, fenetre):
        colonne= board[:,col].reshape(board.shape[0]) # on récupère la colonne 'col' de la matrice board
        a= np.where(colonne== 0) # Liste des élément à 0
        lig= a[0].max() # On prend l'élément le plus profond
        board[lig,col]= self.__couleur # On place le jeton au dessus de la pile à la 1ère case "vide"

        # On vérifie la colonne
        gagne= self.__verif_colonne(lig, col, fenetre, board)
        if gagne== False: # Pas de gagnant sur la colonne, on vérifie la ligne
            gagne= self.__verif_ligne(lig, col, fenetre, board)
            if gagne== False: # Pas de gagnant sur la ligne, on teste les diagonales
                gagne= self.__verif_diag(lig, col, fenetre, board)

        if gagne:
            board[lig,col]= 0
            return col + 1
        else: # on retire le pion
            board[lig,col]= 0
            return -1

    def __verif_colonne(self, lig, col, fenetre, board):
        # On extrait la colonne
        lig2= lig + len(fenetre)
        if lig2 > board.shape[0]: lig2= board.shape[0]
        colonne = board[lig:lig2,col]
        if len(colonne) >= len(fenetre): # On ne teste la colonne que si elle comporte au moins "taille" éléments
            #print(f"colonne: {colonne}\nfenetre: {fenetre}")
            return (colonne== fenetre).all()
        return False

    def __verif_ligne(self, lig, col, fenetre, board):
        # On extrait la colonne
        taille= len(fenetre)
        c1= col - taille + 1
        if c1 < 0: c1= 0 # évite d'avoir un indice de colonne négatifs
        c2= col + taille
        if c2> board.shape[1]: c2= board.shape[1] # évite de déborder: L'indice max est la largeur du board
 
        colonne = board[lig,c1:c2] # Rappel: pour la notation c1:c2 le 1er indice (c1) est inclu, le 2ème (c2) est exclu.
        conv= np.convolve(colonne, fenetre)
        # print(f"Conv: {conv}")
        if taille in conv:
            return True
        return False

    def __verif_diag(self,lig, col, fenetre,board):
        taille= len(fenetre)
        pad_board= np.pad(board, (taille - 1, taille - 1),constant_values= (0, 0))

        # lig et col dans le nouveau référentiel de pad board sont décalé de "taille"
        board_augmente= pad_board[lig : lig + 2 * taille - 1, col : col + 2 * taille - 1]
        diag1= np.diag(board_augmente)

        conv= np.convolve(diag1, fenetre)
        # print(f"Conv: {conv}")
        if taille in conv:
            return True

        board_augmente= board_augmente.T[::-1] # On récupère la diagonale opposée
        diag2= np.diag(board_augmente)
        conv= np.convolve(diag2, fenetre)
        #print(f"diag1: {diag1}\ndiag2: {diag2}")
        #print(f"Conv: {conv}")
        if taille in conv:
            return True

        return False
