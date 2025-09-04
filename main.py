import random, time

number = random.randint(1, 25)
attempts = 0
start_time = time.time()
max_attempts = 10
choice = int(input('Guess a number between 1 and 25: '))

if choice != number:
    attempts += 1
    while choice != number and attempts < max_attempts:
        if choice < number:
            print('Too low!')
        else:
            print('Too high!')
        choice = int(input('Try again: '))
        attempts += 1
    if choice == number:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Congratulations! You guessed the number {number} in {attempts} attempts and {elapsed_time:.2f} seconds.')
    else:
        print(f'Sorry, you have used all {max_attempts} attempts. The correct number was {number}.')