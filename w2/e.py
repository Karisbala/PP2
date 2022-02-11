n, x = map(int, input().split())

arr = []
sum_xor = 0

for i in range(n):
    arr.append(x + 2*i)

for i in range(len(arr)):
    sum_xor = sum_xor ^ arr[i]

print(sum_xor)