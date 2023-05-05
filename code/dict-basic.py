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
num
# %%
e = dict([('python', 1990)])
e
# %%
e = dict([(list('python'), 1990)])

# %%
