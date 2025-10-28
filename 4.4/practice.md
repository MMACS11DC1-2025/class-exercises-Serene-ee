# Guess number bot
# Serene Lee
# Oct 28th, 2025

import random

num = random.choice(range(101))
guess_count = 0

print("Hi, I am a guess number bot. Please enter a guess number between 1-100.")
num1 = int(input())


while num1 != num:

    if num1 == num:
        print("You got it right!")
        guess_count += 1
        break

    elif num1 > num:
        print("The answer is lower than " + str(num1) + ".")
        guess_count += 1

    elif num1 < num:
        print("The answer is higher than " + str(num1) + ".")
        guess_count += 1
    
    print("Please enter another guess number between 1-100.")
    num1 = int(input())

print("You have guessed the right number! It took you " + str(guess_count) + " times to guess it.")