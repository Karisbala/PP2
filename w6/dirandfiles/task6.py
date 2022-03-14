import os
import string

os.mkdir('task6')

for letter in string.ascii_lowercase:
    with open('task6\\'+letter+'.txt', 'w') as file:
        file.write(letter)

file.close()