comp_list = {}

lucky_stud = ''
max_comp = 0

for i in range(int(input())):
    stud_and_comp = input().split()
    if stud_and_comp[0] not in comp_list:
        comp_list[stud_and_comp[0]] = int(stud_and_comp[1])
    else:
        comp_list[stud_and_comp[0]] = comp_list[stud_and_comp[0]] + int(stud_and_comp[1])

for i in comp_list:
    if comp_list[i] > max_comp:
        lucky_stud = i
        max_comp = comp_list[i]

for i in sorted(comp_list):
    if max_comp > comp_list[i]:
        print('{} has to receive {} tenge'.format(i, max_comp - comp_list[i]))
    else:
        print('{} is lucky!'.format(i))
