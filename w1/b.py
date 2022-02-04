s = str(input())
sum = 0
for i in range(len(s)):
    sum += ord(s[i])
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")