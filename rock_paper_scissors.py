
#Rock paper scissors game
#2 Players, each have 3 options to choose from
#Need to decide who wins based on the choices 

import random

#WELCOME
print("Welcome to your virtual ROCK PAPER SCISSORS")

player1_name = input("Please enter your name : ")
print("Welcome ", player1_name)

#round 1 
player_score = 0
computer_score = 0

options = ["rock","paper","scissors"]

while True:

    player1_pick = input("Enter your choice : Rock/Paper/Scissors or Q to quit : ").lower()

    if player1_pick == "q":
        break

    if player1_pick not in ["rock","paper","scissors"]:
        continue

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")

    if player1_pick == "rock" and computer_pick == "scissors":
        print("You Won!")
        player_score += 1
        continue 

    if player1_pick == "rock" and computer_pick == "paper":
        print("You Loose!")
        computer_score += 1
        continue
    if player1_pick == "paper" and computer_pick == "scissors":
        print("You Loose!")
        computer_score += 1
        continue
    if player1_pick == "paper" and computer_pick == "rock":
        print("You Won!")
        player_score += 1
        continue
    if player1_pick == "scissors" and computer_pick == "rock":
        print("You Loose!")
        computer_score += 1
        continue
    if player1_pick == "scissors" and computer_pick == "paper":
        print("You Won!")
        player_score += 1
        continue
    if player1_pick == computer_pick:
        print("Its a tie")
        continue

print("Your final score is ",player_score,"and computer's score is ",computer_score)
  

print("Goodbye")