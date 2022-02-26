import math

print('Input number of sides: ', end = '')
n_sides = int(input())
print('Input the length of a side: ', end = '')
side_length = int(input())

perimeter = n_sides * side_length
apothem = side_length / (2 * math.tan(math.radians(180) / n_sides))

print('The area of the polygon is:', round(perimeter * apothem / 2), sep = ' ')