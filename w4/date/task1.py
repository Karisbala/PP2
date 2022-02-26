'''
Write a Python program to subtract five days from current date.
'''

from datetime import date, timedelta

print(date.today() - timedelta(5))