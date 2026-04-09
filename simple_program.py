"""
A simple Python program that guesses a number
"""
import random

def main():
    """Main function to run the number guessing game"""
    print("Welcome to the Number Guessing Game!")
    print("-" * 40)
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user input
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You found the number {secret_number} in {attempts} attempts!")
                break
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
