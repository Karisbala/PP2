import datetime as dt

date1 = dt.datetime(2017,3,24,0,0,0)
date2 = dt.datetime(2022,3,24,0,0,0)

date_diff = date2 - date1

print(date_diff.total_seconds())
print(date_diff.days * 24 * 3600)