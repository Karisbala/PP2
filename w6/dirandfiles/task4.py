text = open('task4\\text.txt', 'r')
cnt = 0

file_content = text.read()
lines = file_content.split("\n")
  
for i in lines:
    if i:
        cnt += 1
          
print('Number of lines in the text.txt:', end = ' ')
print(cnt)

text.close()