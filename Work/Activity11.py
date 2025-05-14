import random
player_score, dealer_score = 0, 0
print("welcome to BlackJack")

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

while player_score != 3 and dealer_score != 3:
    player_hand, player_value = [], 0
    dealer_hand, dealer_value = [], 0
    
    for _ in range(2):
        player_hand.append(random.choice(list(cards.keys())))
        dealer_hand.append(random.choice(list(cards.keys())))
    
    for card in player_hand:
        player_value += cards[card]
    for card in dealer_hand:
        dealer_value += cards[card]
    
    print(f"Your hand: {player_hand}, Total: {player_value}")
    print(f"Dealer's hand: {dealer_hand}, Total: {dealer_value}")
    
    while True:
        action = input("Do you want to draw or stand? (d/s): ").lower()
        if action == 'd':
            new_card = random.choice(list(cards.keys()))
            player_hand.append(new_card)
            player_value += cards[new_card]
            print(f"You drew a {new_card}. Your hand: {player_hand}, Total: {player_value}")
            if player_value > 21:
                print("You lost! Dealer wins.")
                dealer_score += 1
                break
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")
    
    if player_value <= 21:
        while dealer_value < 17:
            new_card = random.choice(list(cards.keys()))
            dealer_hand.append(new_card)
            dealer_value += cards[new_card]
            print(f"Dealer drew a {new_card}. Dealer's hand: {dealer_hand}, Total: {dealer_value}")
        
        if dealer_value > 21:
            print("Dealer lost! You win!")
            player_score += 1
        elif dealer_value > player_value:
            print("Dealer wins!")
            dealer_score += 1
        elif dealer_value < player_value:
            print("You win!")
            player_score += 1
        else:
            print("It's a draw!")

    print(f"Rounds over! This round score is Player: {player_score} and Dealer: {dealer_score}")
    if player_score == 3:
        print("Congratulations! You win the game!")
    elif dealer_score == 3:
        print("Dealer wins the game!")