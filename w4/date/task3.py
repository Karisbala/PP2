'''
Write a Python program to drop microseconds from datetime.
'''

import datetime

print(datetime.datetime.now().replace(microsecond = 0))