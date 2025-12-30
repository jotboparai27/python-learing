import random

secret_number = random.randint(1, 10)
attempt = 0

while True:

    guess = input("Guess a number between 1 and 10:  ")

    if not guess.isdigit():
        print ("please enter a valid number.")
        continue

    guess = int(guess)
    attempt +=1

    if guess < secret_number:
        print("too low!")
    
    elif guess > secret_number:
        print("too high!")

    else: 
        print(f"Correct! you guessed it in {attempt} tried.")
        break