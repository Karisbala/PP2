discs = []
discs_taken = []

for i in range(int(input())):
    disc = input().split()
    if disc[0] == '1':
        discs.append(disc[1])
    else:
        if len(discs) == 0:
            pass
        else:
            discs_taken.append(discs.pop(0))

print(*discs_taken)