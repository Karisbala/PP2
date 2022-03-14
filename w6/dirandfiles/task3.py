from task1 import list_all_in
import os

print('Please, enter specified path using "/" to check it and print its content:', end = ' ')
path = input()

if os.path.exists(path):
    list_all_in(path)
else:
    print('Path does not exist.')