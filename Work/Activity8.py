import random

words= ["python", "java", "rust", "javascript", "ruby"]
chosen_word = random.choice(words)
list_of_letters = list(chosen_word)
compare_list = list_of_letters.copy()
for i, letter in enumerate(list_of_letters):
    list_of_letters[i] = "_"

print("Let's play a game!")
print("Guess the word", list_of_letters)
attempts = 6
while attempts > 0:
    user_input = input("Enter a letter to guess: ").lower()
    if user_input in compare_list:
        print("Correct guess!")
        for i, letter in enumerate(compare_list):
            if letter == user_input:
                list_of_letters[i] = user_input
        print("Current word:", list_of_letters)
        if list_of_letters == compare_list:
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Gameover! You have {attempts} attempts left.")
        else:
            print("You've run out of attempts. Better luck next time!")
print("The correct word was:", chosen_word)