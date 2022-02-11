import re

s = input().split()

for i in range(len(s)):
    if re.search(r"[ ?!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', s[i]) is None:
        continue
    else:
        s[i] = s[i].replace(s[i], s[i][:-1])

s.sort()
s = list(dict.fromkeys(s))
print(len(s))
for i in s:
    print(i)
