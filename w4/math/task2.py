'''
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''

print('Height: ', end = '')
height = int(input())
print('Base, first value: ', end = '')
base1 = int(input())
print('Base, second value: ', end = '')
base2 = int(input())

print('Expected output: ', round((base1 + base2) * height / 2, 1))

