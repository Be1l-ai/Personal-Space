import random

def jack_en_poy():
    print("Let's play!")
    rock, paper, scissors = 1, 2, 3 
    score = 0
    life = 3
    com_score = 0
    while life != 0 and score != 5:
        try:
            print("Choose 1 for Rock, 2 for Paper, 3 for Scissors")
            user = int(input())
            computer = random.randint(1, 3)
            if user == computer:
                print("It's a tie!")
                continue
            elif user == rock and computer == scissors:
                print("You win! Rock beats Scissors")
                score += 1
                print(f"Your score is: {score}")
            elif user == paper and computer == rock:
                print("You win! Paper beats Rock")
                score += 1
                print(f"Your score is: {score}")
            elif user == scissors and computer == paper:
                print("You win! Scissors beats Paper")
                score += 1
                print(f"Your score is: {score}")
            else:
                print("You lose!")
                life -= 1
                com_score += 1
                print(f"try again, remaining life: {life}")
        except ValueError:
            print("Please enter a number")
            continue
    print("Game ends!!!")
    print(f"You: {score} Computer: {com_score}")
    
jack_en_poy()