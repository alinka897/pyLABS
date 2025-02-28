'''

'''

from collections import deque

def get_min_index():
    path = "/usr/share/nvim/runtime"
    sub_strings = deque(path.split('/'))
    v = min(strings, key=len)
    print(strings, v)

get_min_index()
