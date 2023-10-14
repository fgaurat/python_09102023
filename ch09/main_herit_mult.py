class A:
    def __init__(self,value) -> None:
        self.value = value
    
    def the_method(self):
        print(__class__.__name__,self.value)

class B(A):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = value

    def the_method(self):
        print(__class__.__name__,self.value)

class C(A):
    def __init__(self,value) -> None:
        super().__init__(value)
        self.value = value
    def the_method(self):
        print(__class__.__name__,self.value)


class D(B,C):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = value

    def the_method(self):
        super().the_method()
        super(B,self).the_method()
        print(__class__.__name__,self.value)


from pprint import pprint
pprint(D.mro())
d = D(3)
d.the_method()