import random

secret_number = random.randint(1, 10)
attempt = 0
max_attempts = 5
while attempt < max_attempts:

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

else:
    print(f"Game over ! the number was {secret_number}.")