'''
29. Засунуть вручную путь как список, который состоит из
подстрок разной длины, вывести их, найти самую минимальную
по длине подстроку и дать индекс ее начала.
'''


def get_min_index(path):
    strings = path.split('/')[1:]
    for i in strings:
        print(i, end=' ') if not (i == strings[-1]) else print(i)
    min_val = min(strings, key=len)
    print(path.find(min_val), min_val)


if __name__ == '__main__':
    path = "/usr/share/nvim/runtime"
    get_min_index(path)
