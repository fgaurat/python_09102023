from ICalcGeo import ICalcGeo
import math

class Cercle(ICalcGeo):


    def __init__(self,rayon) -> None:
        super().__init__()
        self ._rayon = rayon

    def get_surface(self):
        return math.pi*self.rayon**2
