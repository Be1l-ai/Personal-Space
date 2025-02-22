import random
def guess_number():
    print("Let's play a game")
    number = random.randint(1, 100)
    while True: 
        try:
            print("Guess a number between 1 and 100")
            guess = int(input())
            if guess < number:
                print("Try again, Number too low")
            elif guess > number:
                print("Try again, Number too high")
            else:
                print(f"You got it, the number was {number}")
                break
        except ValueError: 
            print("Please enter a number")
            continue    
guess_number()