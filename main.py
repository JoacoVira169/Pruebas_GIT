import random
import time

number = random.randint(1, 25)
attempts = 0
start_time = time.time()
max_attempts = 10

def get_valid_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= 25:
                return choice
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

choice = get_valid_input('Guess a number between 1 and 25: ')
#Inicio del bucle
while choice != number and attempts < max_attempts:
    attempts += 1
    if choice < number:
        print('Too low!')
    else:
        print('Too high!')
    choice = get_valid_input('Try again: ')

if choice == number:
    attempts += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Congratulations! You guessed the number {number} in {attempts} attempts and {elapsed_time:.2f} seconds.')
else:
    print(f'Sorry, you have used all {max_attempts} attempts. The correct number was {number}.')