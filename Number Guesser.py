import random

print("Welcome to the Number Guesser Game!")

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))
   
    if guess > 10 or guess < 1:
        print("Invalid number generated. Please try again.")
    
    elif guess == number:
        print("Congratulations! You guessed the number correctly!")    
        break

    else:
        print(f"Sorry, the correct number was {number}. Better luck next time!") 
