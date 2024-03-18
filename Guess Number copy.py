import random
import time
count = 0
def validation():
    global guess
    while guess > int(range) or guess < 1:
        print("You have inputted a value outside of the range.")
        time.sleep(1)
        guess = int(input("Please try again: "))
range = input("Please enter what range you would like to select for the round: ")
time.sleep(1)
print("You have chosen the range of: " + range)
time.sleep(2)
print("How to play: You type in a number, if your number matches the randomly selected number, YOU WIN!")
time.sleep(3)
print("You will get hints based on your guesses along the way.")
time.sleep(2)
print("Try to get to the random number in the least amount of guesses as possible.")
time.sleep(2)
computer = int(random.randrange(1,int(range)))
guess = int(input("Please enter your guess within the range of 1 to " + range + ": "))
validation()
count += 1
while guess != computer:
    if guess > computer:
        print("Your value of " + str(guess) + " is higher than the random number.")
        time.sleep(2)
        guess = int(input("Try again with a lower value: "))
        validation()
    else:
        print("Your value of " + str(guess) + " is lower than the random number.")
        time.sleep(2)
        guess = int(input("Try again with a higher value: "))
        validation()
    count += 1
print("BANG ON, YOU GUESSED THE RIGHT NUMBER!")
time.sleep(1)
print("You got to the random number in " + str(count) + " guesses.")