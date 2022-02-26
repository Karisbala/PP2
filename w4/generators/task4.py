# Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.
a, b = map(int, input().split())

def squares(a, b):
    for i in range(a, b + 1): 
        yield i**2

for i in squares(a, b):
    print(i, end = ' ')