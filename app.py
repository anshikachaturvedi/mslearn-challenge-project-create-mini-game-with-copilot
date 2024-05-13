#import the random module
import random

#create a list of options that has rock, paper, and scissors
options = ["rock", "paper", "scissors"]

#create a score variable and set it to 0
score=0

#create a variable to count the number of rounds
rounds=0

#create a while loop that loops
while True:
    #create a variable that stores the user's choice
    user_choice = input("Enter rock, paper, or scissors: ")

    #create a variable that stores the computer's choice (randomly generated)
    computer_choice=random.choice(options)

    #if the user's choice is rock
    if user_choice == "rock":
        #add the rounds variable by 1
        rounds+=1
        #if the computer's choice is rock
        if computer_choice == "rock":
            print("It's a tie!")
        #if the computer's choice is paper
        elif computer_choice == "paper":
            print("You lose!")
        #if the computer's choice is scissors
        elif computer_choice == "scissors":
            print("You win!")
            #increment the score variable by 1
            score+=1

    #if the user's choice is paper
    elif user_choice == "paper":
        rounds+=1
        if computer_choice == "rock":
            print("You win!")
            score+=1
        elif computer_choice == "paper":
            print("It's a tie!")
        elif computer_choice == "scissors":
            print("You lose!")

    #if the user's choice is scissors
    elif user_choice == "scissors":
        rounds+=1
        if computer_choice == "rock":
            print("You lose!")
        elif computer_choice == "paper":
            print("You win!")
            score+=1
        elif computer_choice == "scissors":
            print("It's a tie!")

    #if the user enters something other than rock, paper, or scissors
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

    #ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    #if the user enters "n"
    # break out of the while loop
    #print out the score and the number of rounds

    if play_again =="n":
        break
    else:
        print("Score: " + str(score))
        print("Rounds: " + str(rounds))

    if play_again == "y":
        continue