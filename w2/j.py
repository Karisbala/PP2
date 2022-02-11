import re

n = int(input())

passwords = []

strong_passwords = []

for i in range(n):
    passwords.append(input())

for i in range(len(passwords)):
    if (re.search(r"\d", passwords[i]) is None) or (re.search(r"[A-Z]", passwords[i]) is None) or (re.search(r"[a-z]", passwords[i]) is None):
        continue
    else:
        strong_passwords.append(passwords[i])

strong_passwords = list(dict.fromkeys(strong_passwords))

print(len(strong_passwords))

for i in strong_passwords:
    print(i)