import random
secret_number = random.randint(1, 100)
attempts = 5
print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")
print("You have", attempts, "attempts.")
while attempts > 0:
 try:
                guess = int(input("Enter your guess: "))
                if guess < 1 or guess > 100:
                     print("Please enter a number between 1 and 100.")
                continue
                if guess < secret_number:
                     print("Too low!")
                elif guess > secret_number:
                     print("Too high!")
                else:
                    print("Correct!")
                    print("Thank You! Your guessing was correct.")
                break
                attempts -= 1
                print("Remaining attempts:", attempts)
                except ValueError:
print("Invalid input! Please enter a number.")
if attempts == 0 and guess != secret_number:
print("Game Over!")
print("The correct number was", secret_number)
print("Thank You For Trying the Game!")
