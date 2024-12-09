
import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else: 
            print("Must be between 2 to 4 players.")
    else:
        print("Invalid Entry, Try again.")    

print(players)


max_score = 50
player_scores = [0 for i in range(players)]


while max(player_scores) < max_score:

    for player_indx in range(players):
        print("\nPlayer number ", player_indx + 1 , "turn has just started!\n")
        print("Your total score is : ", player_scores[player_indx],"\n")
        current_score = 0 

        while True : 

            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over!")
                current_score = 0
                break

            else:
                current_score += value

                print("You rolled a : ", value)    

            print("Your score is : ", current_score)

        player_scores[player_indx] += current_score
        print("Your total score is :",player_scores[player_indx])
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player number",winning_idx + 1,"is the winner with a score of", max_score)

