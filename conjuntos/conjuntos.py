a = set([1,2,3])

a = {0, 1, 2, 3, -1}
b = {2, 3}
c = set([4, 5, 6])

print(a | b) # ou a.union(b)
print(a | c)

print("\n \n")

d = {1, 2, 3, 6}
e = {2, 4, 5, 6}

print(d & e) # ou d.intersection(e)

print("\n \n")

f = {0, 1, 2, 3, -1}
g = {2, 3}

print(f - g) # ou f.difference(g)

print("\n \n")

h = {1, 2, 3, 6}
i = {2, 4, 5, 6}

print(h ^ i) # ou h.symmetric_difference(i)

print("\n \n")

# operações de contido ou não contido

par = {x for x in range(0, 10, 2)}
subpar = {2, 4}

print(par > subpar) # par contém subpar?

print(par < subpar)