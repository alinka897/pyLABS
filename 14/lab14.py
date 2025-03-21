"""
14. Объяснить алгоритм.
Переделать, чтобы файл читался целиком.
"""


def seq_count(file_name, delta):
    import string
    from collections import deque
    from collections import Counter
    st_final = []
    try:
        with open(file_name) as f:
            my_file = f.readlines()
            for line in my_file:
                for slowo in line.split():
                    if len(slowo) < delta:
                        continue
                    elif slowo[0].isdigit() is True:
                        continue
                    else:
                        slowo = slowo.strip(string.punctuation)
                        if slowo[-2:] == '..':
                            slowo = slowo[:-2]
                        slowo = slowo.lower()
                        slowo_d = deque(slowo)
                        while len(slowo_d) >= delta:
                            st_final.append(''.join(slowo_d)[0:delta])
                            slowo_d.popleft()
    except FileNotFoundError:
        print('Нет такого файла')
    print(Counter(st_final).most_common(68))


if __name__ == '__main__':
    seq_count('text.txt', 5)
