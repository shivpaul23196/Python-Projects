
#ASK QUESTIONS : WILL NEED INPUT FOR ANSWER
#IF ANSWER IS RIGHT THEN ADD ONE TO SCORE 
#IF WRONG THEN MENTION THEY GOT IT WRONG


#WELCOME

print("Welcome to my Quiz game");

Playing = input("Do you want to play? ");

if Playing.lower() == "yes":
    
    print("Awesome, let's start the game")
    name = input("Enter name : ")
    print("Welcome " + name + ", Good luck!");
elif Playing.lower() == "no":

    print("Please come back later ");
    exit();
else:
    print("Please enter yes or no response");
    exit();


Score = 0 

question1 = input("What does CPU stand for? ")

if question1.lower() == "central processing unit":
    print("Correct")
    Score += 1;

else:
    print("Wrong Answer");

question2 = input("What does GPU stand for? ")

if question2.lower() == "graphics processing unit":
    print("Correct")
    Score += 1;

else:
    print("Wrong Answer");

question3 = input("What does RAM stand for? ")

if question3.lower() == "random access memory":
    print("Correct")
    Score += 1;

else:
    print("Wrong Answer");

question4 = input("What does PSU stand for? ")

if question4.lower() == "power supply unit":
    print("Correct")
    Score += 1;

else:
    print("Wrong Answer");

question5 = input("What does GB stand for? ")

if question5.lower() == "gigabytes":
    print("Correct")
    Score += 1;

else:
    print("Wrong Answer");

print("Your Final SCORE is ",Score);
print("You got ",(Score/5)*100,"percentage")

