import random

def welcome():
    print("🎯 Welcome to the Guessing Game!")
    print("I'm thinking a number between 1 and 99")
    print("Can you guess that number?")
    print("Let's start!\n")

def get_guess():
    number_to_guess = random.randint(1, 99)
    attempts = 0

    while 1: #or True instead of 1
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Guess is low. Try again!")
            elif guess > number_to_guess:
                print("Guess is high. Try again!")
            else:
                print(f"🎉 Congratulations you guessed it in {attempts} attempts")
                break
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    welcome()
    get_guess()