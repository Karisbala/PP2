n = int(input())

max = 0

arr = list(map(int, input().split()))

ln = len(arr)

for i in range(0, ln):
    for j in range(i + 1, ln):

        prod = arr[i] * arr[j]
    
        if max <= prod:
            max = prod
print(max)