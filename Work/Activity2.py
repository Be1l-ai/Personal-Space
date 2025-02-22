import random

score = 0
life = 3

def word_count():
    global score
    global life
    print("Let's play a game")
    while life != 0:

        sentences = ["I love potato", "I don't love tomato", "I love apple very much", "I hate vegatables they are terrible", "Yokuso watashi no soul society"]
    
        print("Count word per sentence:")
        sentence = random.choice(sentences)
        print(sentence)

        given = sentence.split()
        count = len(given)

        take_answer = input()

        if count == int(take_answer):
            score += 1
            print(f"Your score is: {score}")
        else:
            life -= 1
            print(f"try again, remaining life: {life}")

word_count()