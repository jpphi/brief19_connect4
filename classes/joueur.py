import abc
from abc import ABC, abstractmethod
from random import randint

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

    # Méthode spécifique à la classe Padawan

    def bot_joue(self,colonne_disponible):
        # recuperer le fichier des poids
        pass

class Jedi(Joueur):
    __couleur= 0
    __nom= "Obiwan"
    __recompense= 0
    __TYPE= "JEDI"
    
    def __init__(self,  model, couleur=0, nom= ""):
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            self.model= model
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

    # Méthode spécifique à la classe Jedi

    def jedi_joue(self,colonne_disponible, board, model):
        mat= model.predict(board)
        print(f"model.predict: {mat}")
        col = int(input("colonne: "))

        return col

