import random

words = ["apple", "banana", "cherry", "date", "elderberry"]
chosen_word = random.choice(words)
chosen_word_2 = list(chosen_word)
random.shuffle(chosen_word_2)  
word, attempts = "".join(chosen_word_2), 3

print("Let's play a game!")
print("Guess the shuffled word:", word)
while attempts > 0:
    user_input = input("Enter your guess: ")
    if user_input == chosen_word:
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect! You have {attempts} attempts left.")
        else:
            print("You've run out of attempts. Better luck next time!")
print("The correct word was:" ,chosen_word)