import random

def welcome():
    print("🎯 Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 99")
    print("Can you guess that number?")
    print("Let's start!\n")

def get_random_number():
    return random.randint(1, 99)

def check_guess(guess, number):
    if guess < number:
        return "low"
    elif guess > number:
        return "high"
    else:
        return "correct"

def play_game():
    number_to_guess = get_random_number()
    attempts = 0
    guesses = []

    while 1: #or True instead of 1
        try:
            if guesses:
                print(f"Your previous guesses: {guesses}")

            guess = int(input("Enter your guess: "))
            guesses.append(guess)
            attempts += 1

            result = check_guess(guess, number_to_guess)

            if result == "low":
                print("Guess is low. Try again!")
            elif result == "high":
                print("Guess is high. Try again!")
            else:
                print(f"🎉 Congratulations you guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number")

            # can use match case also
            # match result:
            #       case "low":

if __name__ == "__main__":
    welcome()
    play_game()