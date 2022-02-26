# Implement a generator that returns all numbers from (n) down to 0.
n = int(input())

def reverse_iter(n):
    for i in range(n, -1, -1): 
        yield i

for i in reverse_iter(n):
    print(i, end = ' ')