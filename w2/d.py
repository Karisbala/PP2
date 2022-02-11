def even(n):
    for i in range(0, n):
        print('#', end = '')
        for j in range(1, n):
            if j == i:
                if j == n - 1:
                    print('#')
                else:
                    print('#', end = '')
            elif j > i:
                if j == n - 1:
                    print('.')
                else:
                    print('.', end = '')
            else:
                print('#', end = '')

def odd(n):
    for i in range(0, n):
        if i == n - 1:
            print('#', end = '')
        else:
            print('.', end = '')

        for j in range(1, n):
            if j == i and (i >= (n - 1)/2):
                if j == n - 1:
                    print('#')
                else:
                    print('#', end = '')   
            elif ((i + j) == n - 1):
                if j == n - 1:
                    print('#')
                else:
                    print('#', end = '')  
            elif (i + j) >= n:
                if j == n - 1:
                    print('#')
                else:
                    print('#', end = '') 
            elif j > i:
                if j == n - 1:
                    print('#')
                else:
                    print('.', end = '')
            else:
                print('.', end = '') 

n = int(input())

if n % 2 == 0:
    even(n)
else:
    odd(n)


