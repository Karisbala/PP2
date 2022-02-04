s = str(input())

t = str(input())

lst = []

for i in range(len(s)):
    if s[i] == t:
        lst.append(i)

if len(lst) == 1:
    print(lst[0])
elif len(lst) > 1:
    print(lst[0], lst[-1])    