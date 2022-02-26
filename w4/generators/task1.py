# Create a generator that generates the squares 
# of numbers up to some number N.
n = int(input())

def squar_gen(n):
    for i in range(n): 
        yield i**2

for i in squar_gen(n):
    print(i, end = ' ')