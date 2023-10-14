# import fibo as fb
# from fibo import *
from fibo import fib,fib2
import sys

def fib(r):
    print("bonjour",r)


def main():
    print(sys.argv)
    v = int(sys.argv[-1])

    print("__name__",__name__)
    # fb.fib(12)

    fib(v)
    print(fib2(v))




if __name__=='__main__':
    main()



def main():
    pass

if __name__=='__main__':
    main()

