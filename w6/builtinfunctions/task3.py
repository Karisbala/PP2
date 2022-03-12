s = input()

# t = ''.join(reversed(s))

if s == s[::-1]:
    print('It is palindrome')
else:
    print('It is not palindrome')