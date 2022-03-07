s = input()

t = ''.join(reversed(s))

if s == t:
    print('It is palindrome')
else:
    print('It is not palindrome')