import re

str = input()
match = 'a(b{2,3})'
if re.search(match,  str):
    print('YES') 
else:
    print('NO')

# if str == 'abb' or str == 'abbb':
#     print('YES')
# else:
#     print('NO')