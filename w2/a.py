def jump_to_the_end(arr):
    max_hight = 0
    for i in range(len(arr)):
        if i > max_hight:
            break
        max_hight = max(int(arr[i]) + i, max_hight)
    if max_hight >= len(arr) - 1:
        return 1
    return 0

print(jump_to_the_end(input().split()))