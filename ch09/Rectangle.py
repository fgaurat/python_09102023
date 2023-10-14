from ICalcGeo import ICalcGeo

class Rectangle(ICalcGeo):

    _cpt=0

    def __init__(self,longueur=0,largeur=0) -> None:
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1
    
    @classmethod
    def buildFromStr(cls,value):
        # longueur,largeur = [int(i) for i in value.split("x")]
        # return cls(longueur,largeur)

        values = [int(i) for i in value.split("x")]
        return cls(*values)

    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur
    

    def get_cpt():
        return Rectangle._cpt
    
    @staticmethod
    def set_cpt(value):
        Rectangle._cpt=value

    def __str__(self) -> str:
        return f"{__class__.__name__} longueur:{self._longueur},largeur:{self._largeur}"
    
    def __eq__(self, __value: object) -> bool:
        r = False
        if isinstance(__value,Rectangle):
            r = self._longueur == __value._longueur and self._largeur == __value._largeur
        return r