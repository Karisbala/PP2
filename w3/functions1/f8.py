def spy_game(nums):
    cnt = 0

    for i in nums:
        if i == 0 and cnt == 0:
            cnt = 1
        elif i == 0 and cnt == 1:
            cnt = 2
        elif i == 7 and cnt == 2:
            cnt = 3
            
    return cnt == 3


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))