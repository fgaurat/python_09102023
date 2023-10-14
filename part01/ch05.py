from collections import deque

l = [10,20,30,40]
l.append(50)
print(l)
l.insert(0,0)
print(l)
the_last = l.pop()
print(the_last)
print(l)
the_first = l.pop(0)
print(the_first)
print(l)
d = deque(l)
print(d)
d.appendleft(0)
print(d)
the_first = d.popleft()
print(the_first)
print(d)

print(50*'-')

l = [1,2,3,4]
l2=[]
for i in l:
    l2.append(i*2)

print(l)    
print(l2)
l3=[i*2 for i in l if i > 2]
print(list(range(1,6,2)))
print(l3)
lines = ["   ligne 01  ","ligne 02  ","   ligne 03"]
clean_lines = [l.strip() for l in lines]
print(lines)
print(clean_lines)


print(l)
del l[1]
# l.remove(2)
print(l)


print(50*'-')


def f():

    return 0,1,2


a,b,c = f()

t = "value 01","value 02","value 03"
a,b,*c,d=0,1,3,4,5


# a,b,c=0,1
# print(a,b,c,d)

# t[0]="tutu"

s = {12,34,12,65,34,12}
s = {'toto','tutu','toto','titi',12}
print(s)

s1 = {2,3,4,5}
s2 = {12,3,54,5}

print(s1-s2)

# l1 = [2,3,4,5]
# l2 = [12,3,54,5]
# print(l1-l2)

print(3 in s1)
print(l)
print(3 in l)


print(50*"-")

d = {
    "name":"GAURAT",
    "firstName":"Fred",
    "age":47,
    "languages":[
        "Python",
        "JS",
    ]
}
print(d)
print(d['firstName'])
d['city']="Sainte genevieve ..."
print(d)

for k,v in d.items():
    # print(k,d[k])
    print(k,v)

l = ["Value 01","Value 02","Value 03","Value 04"]

# for i in range(len(l)):
for i,v in enumerate(l):
    print(i,v)