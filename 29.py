from collections import deque

path = "/usr/share/nvim/runtime"
strings = deque(path.split('/'))
v = min(strings, key=len)
print(strings, v)
