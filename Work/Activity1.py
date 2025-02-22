import random

score = 0  

def math_prob(): 
    global score
    while True:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        ope = random.choice(["+", "-", "*"])
        
        prob = f"What's {num1} {ope} {num2}?"
        print(prob)
        
        try:
            take = int(input())
            answer = eval(f"{num1} {ope} {num2}")
            
            if take == answer:
                print("Correct!")
                score += 1
                print(f"Score: {score}")
            else:
                print(f"Game over! The correct answer was {answer}.")
                print(f"Final score: {score}")
                break
            
        except ValueError:
            print("Error")

math_prob()