import random

def guesser():
    print('Hello! What is your name?')
    name = input()
    print('Well, {}, I am thinking of a number between 1 and 20.'.format(name),'Take a guess.', sep = '\n')
    g = 0
    rn = random.randint(1, 20)

    while True:
        n = int(input())
        if n < rn:
            print('Your guess is too low.', 'Take a guess.', sep = '\n')
            g += 1
        elif n > rn:
            print('Your guess is too high.', 'Take a guess.', sep = '\n')
            g += 1
        else:
            print('Good job, {}! You guessed my number in {} guesses!'.format(name, g))
            break

# guesser()