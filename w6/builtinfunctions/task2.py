import re

s = input()

up = re.findall(r'[A-Z]', s)
low = re.findall(r'[a-z]', s)

print('The number of upper case letters: {} \nThe number of lower case letters: {}'.format(len(up),len(low)))

