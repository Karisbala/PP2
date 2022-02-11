from datetime import datetime

prof_dates = []

while True:
    date = input()
    if date == '0':
        break
    prof_dates.append(date)
    
prof_dates.sort(key=lambda date: datetime.strptime(date, '%d %b %Y'))

for i in range(len(prof_dates)):  
    print(prof_dates[i]) 