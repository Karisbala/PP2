import os
from fnmatch import fnmatch

# print('Please, enter specified path using "/" to list its content:', end = ' ')
# root = input()

def list_all_in(root):
    pattern = "*.*"

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                print(os.path.join(path, name))

def print_content(level, path):
    for x in os.listdir(path):
        for i in range(level + 1):
            print('======',end='')
        print(x)
        if os.path.isdir(path + "/" + x):
            print_content(level + 1, path + "/" + x)

# print('''
# ____________________________

# First method:
# ____________________________
# ''')
# list_all_in(root)



# print('''
# ____________________________

# Second method:
# ____________________________
# ''')
# print_content(0, root)