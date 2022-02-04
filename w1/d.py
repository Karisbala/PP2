n = int(input())
z = str(input())

def kilo_to_bytes(n):
    print(n*1024)

def bytes_to_kilo(n, c):
    print(round(float(n/1024), c))

if z == "b":
    kilo_to_bytes(n)
elif z == "k":
    c = int(input())
    bytes_to_kilo(n, c)