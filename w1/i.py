n = int(input())
lst = []
while n:
    s = str(input())
    if s[-10:] == "@gmail.com":
        s = s.replace('@gmail.com', '')
        lst.append(s)
    n -= 1

for i in lst:
    print(i)

