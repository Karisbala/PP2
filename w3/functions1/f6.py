def reverse(s):
    s = s.split()
    return s[::-1]

s = reverse(input())

for i in s:
    print(i, end = ' ')