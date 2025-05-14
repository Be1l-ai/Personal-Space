import random
score1 = 0
score2 = 0
print("Let's play High Card Game!!!")
print("First player to score 3 wins the game!")


while score1 != 3 and score2 != 3:
    input("Player 1 please select Enter to draw a card...")
    player1 = random.choice(range(1,14))
    input("Player 2 please select Enter to draw a card...")
    player2 = random.choice(range(1,14))
    print(f"Player 1 draws {player1}, while Player 2 draws {player2}")
    if player1 > player2:
        print("Player 1 win the round")
        score1 +=1
        print(f"Player 1 score is: {score1}")
    elif player2 > player1:
        print("Player 2 win the round")
        score2 +=1
        print(f"Player 2 score is {score2}")
    else:
        print("It's a draw")

print(f"Game's Up the final score is Player 1 : {score1} and Player 2 : {score2}")