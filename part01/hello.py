import copy

print("Hello")


# TheWorldIsFlat => UpperCamelCase
# theWorldIsFlat => camelCase
# the_world_is_flat => snake_case
# the-world-is-flat => kebab-case

the_world_is_flat = True
if the_world_is_flat:
    print("Toto careful not to fall off!")
a = "2"
i = int(a)
print(type(a))
print(type(i))

s = 'L\'orange gronde'
s = "L'orange gronde"
s1 = "Ligne 01\nLigne 02"
print(s1)
p = "c:\\tmp\\newvalue"
p = r"c:\tmp\newvalue"
print(p)

lines = """Ligne 01
Ligne 02
Ligne 03
"""
print(lines)

a = 4
print(50*'-')
print("a="+str(a))
print("toto"*a)

s = "Python"
print(s[2])
print(s)
print(len(s))
print(s[len(s)-1])
print(s[-1])

print(s[0:4])
print(s[4:5])
print(s[:5])
print(s[3:])
print(s[3:435])

s = "Python"
# s[0] = "J"
s = "Jython"
print(s)

i = 2
print(hex(id(i)))

i = 3
b = 3
print(hex(id(i)))
print(hex(id(b)))

print(50*'-')

squares = [1, 4, 9, 16, 25]
print(squares)

squares2 = squares[:]
squares[0] =1000
print(squares)
print(squares2)

print(50*'-')
l = [
    [10,20],
    [30,40],
    [50,60],
]
print(l)
# l2 = l[:]
# l2 = l.copy()
# l2 = copy.copy(l)

l2 = copy.deepcopy(l)

l[1][1] = 1000
print(l)
print(l2)
squares2.append(36)
print(squares2)

print(50*'-')
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

