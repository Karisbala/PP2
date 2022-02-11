n = int(input())

for i in range(0, n):
    print(i, end = ' ')
    for j in range(1, n):
        if j > i and j > 1 and i >= 1 and not j == i:
            if j == (n - 1):
                print(0)
            else:
                print(0, end = ' ')
        elif j < i and i > 1 and j >= 1 and not j == i:
            print(0, end = ' ')
        elif i == j:
            print(i*j, end = ' ')
        elif j == (n - 1):
            print(j)
        elif i == 0:
            print(j, end = ' ')
              
            
