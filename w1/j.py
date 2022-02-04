s = str(input())

lst = s.split()

for i in lst:
    if len(i) >= 3:
        print(i, end = " ")