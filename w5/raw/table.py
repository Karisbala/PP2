import re
import csv

file = open('row.txt','r')
text = file.read()

# BINPattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'
# SMPattern = r'\nСмена.*(?P<SM>\b[0-9]+)'

# BINText = re.search(BINPattern, text).group("BIN")
# SMText = re.search(SMPattern, text).group("SM")

ItemPatternText = r'(?P<Name>.*)\n{1}(?P<Count>.*)\sx\s(?P<Price>.*)\n{1}(?P<Total>.*)'
ItemPattern = re.compile(ItemPatternText)


rows = [["Название","Кол-во", "Цена", "Стоймость"]]

for m in re.finditer(ItemPattern, text):
    rows.append([m.group("Name"),m.group("Count"),m.group("Price"),m.group("Total")])

receipt_total_pattern = r'ИТОГО:\n(?P<Total2>\b.+\n)'
receipt_total_text = (re.search(receipt_total_pattern, text).group('Total2')).strip()

rows.append(['','','Итого:', receipt_total_text])

with open('data.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)