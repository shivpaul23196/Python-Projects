import random 

upper_range = input("Type a Number: ")

if upper_range.isdigit():
    upper_range = int(upper_range)

    if upper_range <= 0:
        print("Please type a number larger than 0 next time")
        exit()
else:
    print("Please type a number next time.")
    exit()        


random_num = random.randint(0, upper_range)
print(random_num)

guesses = 0 

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
            user_guess = int(user_guess)
    else:
        print("Please type a number next time.")        
        continue

    if user_guess == random_num:
        print("You got it in",guesses,"guesses")
        
        break

    elif user_guess < random_num:
            print("Your guess is lower than the random number")
            print("You got it wrong!")
    
    else:
            print("Your guess is higher than the random number")
            print("You got it wrong!")
        
        