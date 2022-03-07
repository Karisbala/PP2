import re

str = input()
match = r'a(.*)(b$)'
if re.search(match,  str):
    print('YES') 
else:
    print('NO')