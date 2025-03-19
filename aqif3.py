import math
import random

lBound = int(input("Enter Lower bound:  "))
uBound = int(input("Enter Upper bound:  "))
number_of_chances = 3
print(f"\n\tYou've only {number_of_chances} chances to guess the integer!\n")

random_number = random.randint(lBound, uBound)

count = 0
while count < number_of_chances:
    count += 1
    guess = int(input("Guess a number: "))
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print(count)
        print("Congratulations! You've guessed the correct number!")
        break

print(f"\nThe number is {random_number} ")