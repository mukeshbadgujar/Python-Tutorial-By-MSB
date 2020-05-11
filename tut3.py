# n = 5
# print(id(n))
'''n = 6
print(id(n))'''

n = 5
m = n
print(id(m))
print(id(n))
m = 6
n = m
print(id(m))
print(id(n))

IP = 3.14

a = 4.8
b = a
print(int(b))

a = 4
b = a
print(float(b))

k = 7
c = complex(a,k)
print(c)
