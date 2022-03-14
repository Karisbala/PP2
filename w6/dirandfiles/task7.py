file1 = open('task7\\text.txt', 'r')

content = file1.read()

with open('task7\\text_copy.txt', 'w') as file2:
    file2.write(content)

file1.close()
file2.close()