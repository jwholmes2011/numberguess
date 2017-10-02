import random

BOUNDS = (1, 50)
TRIES_ALLOWED = 5

the_number = random.randint(*BOUNDS)

print("\tYou're playing 'Guess the Number'!\n")
print("The number I'm thinking of is between %d and %d." % BOUNDS)
print("You only have so many attempts, so guess well.\n")

for tries in range(TRIES_ALLOWED):
    guess = int(input("What's your guess: "))

    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    else:
        print("You got it! The number was %d" % (the_number))
        print("Congratulations! It only took you %d tries!\n\n" % (tries + 1))
        break
else:
    print("You failed to guess in time!\n\n")

# Admittedly a contorted way to write a statement that works in both Python 2 and 3...
try:
    input("Press the enter key to exit.")
except:
    pass
