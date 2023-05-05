# %%
help(dict)

# %%
a = {'python': 1990, 'c': 1972}
a

# %%
type(a)

# %%
b = dict((('python', 1990), ('c', 1972)))
b

# %%
c = dict([('python', 1990), ('c', 1972)])
c

# %%
a['python'] = 1989
a

# %%
a['c#'] = 2000
a

# %%
for i in a:
    print(i)

# %%
for k in a:
    print(k, a[k])

# %%
num = dict(one=1, two=2)
num

# %%
num['three'] = 3
num

# %%
for k in num:
    print(k, '->', num[k])

# %%
num2 = dict() # {}
type(num2)

# %%
for k in num:
    num2[num[k]] = k
num2

# %%
import math
math.pi

# %%
math.e

# %%
help(round)

# %%
round(math.e, 2)

# %%
round(math.pi, 3)

# %%
p = dict(apple=0.4, orange=0.35, banana=0.25)
p

# %%
for k, v in p.items():
    p[k] = round(v * 0.9, 2)
p
# %%
for i in p.items():
    p[i[0]] = round(i[1] * 0.9, 2)
p

# %%
lst = [1, 2, 3]
a, b, c = lst
c

# %%
data = lst
print(data[0], data[1], data[2])

# %%
p
# %%
p2 = {}
for k, v in p.items():
    p2[v] = k
p2

# %%
p
# %%
p3 = {}
for k, v in p.items():
    if v <= 0.3:
        p3[v] = k
p3

# %%
c = { i: i**i for i in range(5)}
c

# %%
