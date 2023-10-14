# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


l = ["value 01","value 02","value 03","value 04"]
for value in l:
    print(value)


for i in range(len(l)):
    print(str(i)+" : "+l[i]) # 0 : value01
    print(i,":",l[i]) # 0 : value01

print(range(4,12,2))
print(list(range(4,12,2)))

print(list(range(3)))

print(50*'-')

values = range(12)
to_find = 5

found = False
for v in values:
    if v == to_find:
        found = True
else:
    print("pas trouvé")


if found:
    pass
else:
    print("KO")

# r = found?"OK":"KO"
# print("OK" if found else "KO")

# ok si trouvé sinon ko
print(50*'-')


def fib(n:int=12):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n:int)->list:    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    the_values = []
    a, b = 0, 1
    while a < n:
        the_values.append(a)
        a, b = b, a+b
    print(hex(id(the_values)))
    return the_values

r = fib(12)
print(r)

r = fib2(12)

print(hex(id(r)))
r = fib2(12)
print(hex(id(r)))
print(r) # [0,1,1,2,3,5,8] 

a = 2
print(type(a))
a = fib2
print(type(a))


fib()
r = fib2(12)
print(r)


def hello(name,firstName:str="Henri",age:int=40):
    """
    print bonjour
    """
    print("Bonjour","name",name,"firstName",firstName,"age",age)



hello("GAURAT","Frédéric")
hello(firstName="Frédéric",name="GAURAT")
hello("GAURAT",age=54)

print(50*'-')

def add(*values):# [10,20,30,40]
    # (10,20,30,40)
    print(values)
    r=0
    for v in values:
        # r=r+v
        r+=v
    return r    


v = [10,20,30,40]

# r = add(v) # 100
# print(r)

r = add(10,20,30,40)
print(r)
r = add(*v)
print(r)
print(50*'-')

def hello(**values):
    # {firstName:"Frédéric",name:"GAURAT",age:47}
    print(values.keys())
    print(values.values())
    print(values.items())
    """
    print bonjour
    """
    print("Bonjour","name",values['name'],"firstName",values['firstName'],"age",values['age'])
    pass


hello(firstName="Frédéric",name="GAURAT",age=47)


# print("Hello","fred",47,sep="-",end="end")


def f(*args,**kwargs):
    print(args)
    print(kwargs)


f(1,2,3,value="toto",value1="tutu")

print(50*'-')

values = [1,2,3,4]

def mult2(the_values):
    r =[]
    for i in the_values:
        r.append(i*2)
    return r

def mult2_map(item):
    return item *2

result = mult2(values) # [2,4,6,8]
print(result)

m = lambda i:i*2
result = list(map(m,values))

print(result)
