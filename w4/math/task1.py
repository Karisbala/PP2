'''
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
'''


import math

degree = int(input())

print(round(degree * math.pi / 180, 6))