"""
Set a dictionary with 4 items,
value of each is a list with 5 integers.
Print the item with minimal sum.
"""

import random

d = {x: [random.randint(-100,100) for i in range(5)] for x in range(4)}
print(d)
for k, v in d.items():
    if v == min(d.values(), key = sum):
        print(k, v)
