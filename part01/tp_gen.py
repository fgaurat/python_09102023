

def gen_values():
    # l = [i for i in range(1_000_000)]
    # return l 
    for i in range(1_000_000):
        yield i


def main():
    y =  gen_values()

    print(y)
    # for item in y:
    #     print(item)

if __name__=='__main__':
    main()

