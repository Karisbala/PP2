# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n = int(input())

def even_gen(n):
    for i in range(0, n + 1, 2): 
        yield i

for i in even_gen(n):
    if i < n - 1:
        print(i, end = ', ')
    else:
        print(i)