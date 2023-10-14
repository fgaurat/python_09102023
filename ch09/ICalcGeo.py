from abc import ABCMeta,abstractmethod

class ICalcGeo(metaclass=ABCMeta):

    @abstractmethod
    def get_surface(self):
        pass


class IOldCalcGeo():

    def get_surface(self):
        raise NotImplementedError("get Surface !!!")