import abc
from abc import ABC, abstractmethod

class Joueur(ABC):
    _couleur_dispo=[-1,1]

    @abstractmethod
    def nom(self):
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
    
    def __init__(self, couleur, nom= ""):
        if couleur in self._couleur_dispo:
            self.__couleur= couleur
            self.__nom= f"{self.__nom}-{couleur}"
            self._couleur_dispo.remove(couleur)
            print(self._couleur_dispo)
            
        else:
            print(f"La couleur doit appartenir à la liste {self._couleur_dispo}.")

       
    def nom(self):
        return self.__nom
    
    def get_couleur(self):
        return self.__couleur
    
    def recompense(self, gain):
        self.__recompense+= gain
        
    def get_recompense(self):
        return self.__recompense
