import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10 


def generate_problems():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left) + " " + operator + " " + str(right) 
    answer = eval(exp)
    return exp,answer


wrong = 0 
input("Press Enter to start")
print("-------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    exp,answer = generate_problems()
    while True:
        guess = input("Problem #" +  str(i + 1) + ": " +  exp + " =" )
        if guess == str(answer):
            break
        wrong += 1 

end_time = time.time()

total_time = round(end_time - start_time,2)


print("-------------------")
print("Good job! You finished in Total time of :", total_time, "Seconds")
