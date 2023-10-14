import traceback

def div(a,b):
    return a/b

def call_div(a,b):
    try:
        print(f'LOG {a},{b}')
        r = div(a,b)
        print(f'LOG {a}/{b} = {r}')
    finally:
        print("Close log file")
    return r


def main():
    
    try:
        a=2
        # b=int(input('b:'))
        b=0
        c = call_div(a,b)
        print(c)

    # except ZeroDivisionError as e:
    #     print("Erreur ZeroDivisionError",e.__class__.__name__)
    # except TypeError as e:
    #     print("Erreur TypeError",e)
    # except ValueError as e:
    #     print("Erreur ValueError",e)
    except Exception as e:
        print("Erreur",e,e.__class__.__name__)
        traceback.print_exc()
    else:
        print("pas d'erreur")
    print("après")

if __name__=='__main__':
    main()
