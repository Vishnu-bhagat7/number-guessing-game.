import random

#Computer picks a random number between 1 to 100
secret_number = random.randint(1, 100)

print("I have chosen a number between 1 to 100.")
print("Can you guess it?")

attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! try again.")
    elif guess > secret_number:
        print("Too high! try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} tries.")
        break