import random

def get_vail_guess():
    while True:
        guess = input("Guess a number between 1 and 10: ")

        if guess.isdigit(): 
            return int(guess)
        
        print("Please enter a valid number.")

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0 
    max_attempts = 5

    while attempts < max_attempts:
        guess = get_vail_guess()
        attempts +=1 

        if guess < secret_number:
            print("too low!")
        elif guess > secret_number:
            print("too high!")
        else: 
            print(f"Correct! you guessed it in {attempts} tries.")
            return
    print(f" Game over! the number was {secret_number}.")

play_game()