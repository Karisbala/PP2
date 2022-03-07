import re

str = input()
match = r'[A-Z]+[a-z]+'
seq = re.findall(match,  str)

if seq:
    print(seq) 
else:
    print('NO')