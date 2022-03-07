import re

str = input()
match = r'[a-z]+_[a-z]+'
seq = re.findall(match,  str)

if seq:
    print(seq) 
else:
    print('NO')