#Buit In Data types
a = "ray" 
b = 1
c = 1.23
d = 78j
e = ['Morning', 'Afternoon', 'Evening']
f = ('Morning', 'Afternoon', 'Evening')
g = range(10)
h = {"name" : "ray", "age" : 21}
i = {'Morning', 'Afternoon', 'Evening'}
j = frozenset({'Morning', 'Afternoon', 'Evening'})
k = True
l = b"ray"
m = bytearray(5)
n = memoryview(bytes(5))

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))

#Specific data type

A = str("ray")
B = int(3)
C = float(5.6)
D = complex(45j)
E = list(("Morning", "Noon", "Evening", "Night"))
F = tuple(["Morning", "Noon", "Evening", "Night"])
G = range(32)
H = dict(name="ray", age=21)
I = set({"Morning", "Noon", "Evening", "Night"})
J = frozenset({"Morning", "Noon", "Evening", "Night"})
K = bytes(5)
L = bytearray(66)
M = memoryview(bytes(32))
N = bool(65)

print(type(A))
print(type(B))
print(type(C))
print(type(D))
print(type(E))
print(type(F))
print(type(G))
print(type(H))
print(type(I))
print(type(J))
print(type(K))
print(type(L))
print(type(M))
print(type(N))