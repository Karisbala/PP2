def uniq(list1):
    return list(dict.fromkeys(list1))

list1 = input().split()

print(uniq(list1))