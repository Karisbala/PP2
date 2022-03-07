import math
from time import sleep

n = int(input())
d = int(input())

n_sqrt = math.sqrt(n)

sleep(d / 1000)

print('Square root of {} after {} miliseconds is {}'.format(n, d, n_sqrt))