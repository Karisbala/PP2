import re

str = input()
match = '^a(b*)$'
if re.search(match,  str):
    print('YES') 
else:
    print('NO')