import sys
n, f = map(int, input().split())

if n <= 500:
    for i in range(2, n):
        if (n % i) == 0:
            print("Try next time!")
            sys.exit()
    if f % 2 == 0:
        print("Good job!")
    else:
        print("Try next time!")
else:
    print("Try next time!")
