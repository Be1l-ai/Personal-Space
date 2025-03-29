import random
import time

print("Let's play a game!")
sequence, attempts = random.sample(range(1, 100), 5), 3
print("Memorize the following sequence of numbers:")
print(sequence)
time.sleep(3)
print("\n" * 100) 
while attempts > 0:
    user_input = input("Enter the numbers separated by spaces: ")
    try:
        user_sequence = list(map(int, user_input.split()))
        if user_sequence == sequence:
            print("Congratulations! You won.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left.")
            else:
                print("You've run out of attempts. Better luck next time!")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
print("The correct sequence was:", sequence)