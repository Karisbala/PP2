def solve(numheads, numlegs):

    return ((numlegs) - 2 * (numheads)) / 2

numheads = 35
numlegs = 94

rabbits = int(solve(numheads, numlegs))

print("Rabbits =", rabbits)
print("Chickens =", numheads - rabbits)