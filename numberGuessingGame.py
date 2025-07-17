import random
print("Welcome to the Number Guessing Game!" \
"Choose your difficulty level: " \
      "1. Noob (1-10) " \
      "2. Pro (1-100) " \
      "3. Hacker (1-1000)")
difficulty = int(input("Enter difficulty level (1, 2, or 3): "))
guess = 0
attempts = 0
if difficulty == 1:
    secret = random.randint(1, 10)
    maxNumber = 10
elif difficulty == 2:
    secret = random.randint(1, 100)
    maxNumber = 100
elif difficulty == 3:
    secret = random.randint(1, 1000)
    maxNumber = 1000
else:
    print(f"Invalid difficulty level. Defaulting to Pro (1-100).")
    secret = random.randint(1, 100)
while guess != secret:
    guess = int(input(f"Guess a number between 1 and {maxNumber}: "))
    if guess < secret:
        print("Too low! Try again.")
        attempts += 1
    elif guess > secret:
        print("Too high! Try again.")
        attempts += 1
    elif guess == secret:
        attempts += 1
        break
print(f"Congratulations! You've guessed the number correctly. After {attempts} attempts, the secret number was {secret}.")