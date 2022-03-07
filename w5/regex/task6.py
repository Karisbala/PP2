import re

str = input()

rep = re.sub('[  . ,]',  ':', str)
if rep:
    print(rep) 
else:
    print('NO')