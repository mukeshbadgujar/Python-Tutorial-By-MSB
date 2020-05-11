# Lists  (mutable/Chamgable)

n = [8, 3, 1, 5, 2, 5]
print(n)
print(n[3])
print(n[2:])

n = ["MSB","DD","RPS","AA"]
print(n)
print(n[3])
print(n[2:])

n.append("HH")
print(n)

n.insert(1,"QQ")
print(n)

n.remove("AA")
print(n)

n.pop(2)
print(n)

n = ["MSB","DD","RPS","AA"]
del n[:-2]
print(n)

n = [8, 3, 1, 5, 2, 5]
n.extend([9,8,7,6,5])
print(n)
# -----------------------Above Str or Number

n = [8, 3, 1, 5, 2, 5, 9]
print(max(n))
print(min(n))
print(sum(n))

n = [8, 3, 1, 5, 2, 5, 9]
print(sorted(n))  # For String also
print(n)

n = [8, 3, 1, 5, 2, 5, 9]
n.sort() # For String also
print(n)
print(n)

print(len(n))

#*******************************************

# Tuple  (Inmutable/ Not Changable)

t = (1,5,2,8,2,2,4,2)
print(t)
print(t[3])
print(t.count(2))
print(t.index(4))

# Set
s = {22, 55, 66, 8, 18, 9}
s2 = {8, 18, 9, 99, 32}
print(s)

s.add(44)
print(s)

s.remove(8)
print(s)

s.pop()
print(s)

s = {22, 55, 66, 8, 18, 9}
s2 = {8, 18, 9, 99, 32}
s.intersection(s2)
print(s)



