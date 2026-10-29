# Python Assignment 3: Loops and Functions

import random

def number_guessing_game():
    print("\n--- Part 1: Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 3
    
    while attempts > 0:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
            
        if guess < 1 or guess > 10:
            print("Your guess is out of range. Please guess a number between 1 and 10.")
            continue
            
        attempts -= 1
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
    else:
        print(f"Better luck next time! The correct number was {secret_number}.")

def multiplication_table_generator():
    print("\n--- Part 2: Multiplication Table Generator ---")
    try:
        num = int(input("Enter the number for which you want the multiplication table: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Please enter a valid integer.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_calculator_interface():
    print("\n--- Part 3: BMI Calculator ---")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    # To run a specific exercise, you can comment/uncomment the functions below
    number_guessing_game()
    multiplication_table_generator()
    bmi_calculator_interface()
