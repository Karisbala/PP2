def filter_prime(i, list1):
    for j in range(2, int(list1[i])):
        if int(list1[i]) % j == 0:
            return
        else:
            return list1[i]

list0 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14'
list1 = list0.split()

for i in range(len(list1)):
    n = filter_prime(i, list1)
    if n is None:
        continue
    else:
        print(n, end = ' ')


# list2 = []
# for i in range(len(list1)):
#     n = filter_prime(i, list1)
#     if n is None:
#         continue
#     else:
#         list2.append(n)
# for i in range(len(list1)):
#     print(list2[i])