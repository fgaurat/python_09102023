from Rectangle import Rectangle
from Carre import Carre


def main():
    r = Rectangle(1,3)
    print(r.get_surface())
def main02():
    r = Rectangle(1,3)
    r.longueur = 12
    print(r.longueur,r.largeur)
    c = Carre(2)
    print(c.get_surface())
    c.cote= 12
    print(c.get_surface())
    print(c)

    print(Carre.mro())
    

    
def oldmain():
    r = Rectangle(2,3)
    r1 = Rectangle(12,3)
    r2 = Rectangle(12,35)
    lng = r.get_longueur()
    lrg = r.get_largeur()
    print(lng) #2
    print(lrg) #3
    r.set_longueur(12)
    print(r.get_longueur())#12
    print(r.get_surface()) # 36
    print(Rectangle.get_cpt())
    Rectangle.set_cpt(10)
    r.set_cpt(10)
    print(Rectangle.get_cpt())

    r3 = Rectangle()
    print(id(r3))
    # print(r3.get_largeur())
    r3 = r3.buildFromStr("2x5")
    r3 = Rectangle.buildFromStr("2x5")
    print(id(r3))
    print(r3.get_longueur(),r3.get_largeur())
    print(50*'-')
    s = str(r3)
    print(s)
    r1 = Rectangle(12,3)
    r2 = Rectangle(12,3)

    # if r1.__eq__(r2):
    if r1==1:
        print('ok')
    else:
        print('ko')


    print(r1.longueur) 
    r1.longueur =-12 # r1.set_longueur()

if __name__=='__main__':
    main()
