import os

def get_files():
    root_dir = input("Введите абсолютный путь первой папки: ")
    command = 'ls {} -R >> files.txt'.format(root_dir)
    os.system(command)

get_files()
