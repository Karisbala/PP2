s = str(input())
s = list(s)

def toLowercase(s):
    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':
            s[i] = chr(ord(s[i])+32)

toLowercase(s)

s = ''.join(s)

print(s)