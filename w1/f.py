n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

for i in arr:
    if i <= 10:
        print("Go to work!")
    elif (i > 10) and (i <= 25):
        print("You are weak")
    elif (i > 25) and (i <= 45):
        print("Okay, fine")
    elif i > 45:
        print("Burn! Burn! Burn Young!")