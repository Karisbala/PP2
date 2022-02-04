def binToDec(n):

    if n == 0:
        return 0
    else:
        return (n % 10 + 2 * binToDec(n // 10))

n = int(input())

print(binToDec(n))