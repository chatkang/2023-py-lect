# %% How to Use Generators and yield in Python
a = range(5)
a

# %%
list(a)

# %%
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
next(gen)

# %%
next(gen)
# %%
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

print(nums_squared_lc)
print(nums_squared_gc)

# %%
import sys
nums_squared_lc = [i ** 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))

# %%
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

# %%
sum([i * 2 for i in range(10000)])
    
# %%
import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')

# %%
cProfile.run('sum((i * 2 for i in range(10000)))')

# %%
letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)   

# %%
help(iter)

# %%
