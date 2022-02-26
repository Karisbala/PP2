from datetime import date, timedelta

print('Yesterday was: ', date.today() - timedelta(1))
print('Today is: ', date.today())
print('Tomorrow will be: ', date.today() + timedelta(1))