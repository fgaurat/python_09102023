



a = [2,3,4]
r =3
def main(b):
    # global a
    a=[123,432,543]
    b.append(1000)
    print("main",a)
    if r==3:
        t = 12
        print('ok')
    print("t",t)

print("after",a)



if __name__=='__main__':
    b = [45,67]
    print(b)
    main(b)
    print(b)
    print("after main",a)