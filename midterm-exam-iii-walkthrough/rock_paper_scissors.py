"""
@author: <Your name>
date: <today's date>
Project code name: HandBattle
Purpose:
    A program that play rock, paper, scissor
"""

import datetime
import random

ROCK = "rock"
PAPER = "paper"
SCISSOR = "scissor"

#PREDEFINED
"""
    This function will print the header containing 
    Rock, paper,scissor as well as today's date and time
"""
def game_header():
    print("==============================")
    rock = "Rock:🗿"
    paper = "Paper:📃"
    scissor = "scissor:✂️"
    print(f"{rock} {paper} {scissor}")
    print("\n\tGame Version 0.1")
    print("==============================\n")
    now = datetime.datetime.now()
    print("Date and Time:",now.strftime("%d/%m/%Y %H:%M:%S"))

#PREDEFINED
"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        round: The current round in the game

    returns the xp for the round
"""
def generate_xp(round):
    min_xp = 1
    max_xp = 30
    xp = random.randint(min_xp, max_xp)
    return xp * round

#PREDEFINED
"""
    This function will randomly pick a choice for the computer.
    This will return one of the following, "rock", "paper" or "scissor"
"""
def get_computer_choice():
    choices = [ROCK, PAPER, SCISSOR]
    return random.choice(choices)


#STUDENT CODE HERE
#STUDENT FUNCTIONS HERE
def determine_winner(player_choice, computer_choice):
    if player_choice == ROCK and computer_choice == SCISSOR:
        return "player"
    elif player_choice == PAPER and computer_choice == ROCK:
        return "player"
    elif player_choice == SCISSOR and computer_choice == PAPER:
        return "player"
    
    elif computer_choice == ROCK and player_choice == SCISSOR:
        return "computer"
    elif computer_choice == PAPER and player_choice == ROCK:
        return "computer"
    elif computer_choice == SCISSOR and player_choice == PAPER:
        return "computer"
    
    elif player_choice == computer_choice:
        return "tie"
    
    else:
        return None
    
    # A Shorter way to write the game logic
    # if (player_choice == "rock " and computer_choice == SCISSOR) or  (player_choice == PAPER and computer_choice == ROCK) or     (player_choice == SCISSOR and computer_choice == PAPER):
    #     return "player"
    
    # elif player_choice == computer_choice:
    #     return "tie"
    
    # else:
    #     return "computer"

def get_user_choice():
    while True:
        user_choice = input("Enter Choice - Rock, Paper, or scissor: ").lower()

        if user_choice == ROCK or user_choice == PAPER or user_choice == SCISSOR:
            return user_choice
        
        print("Invalid choice")

#PREDEFINED
def main():
    #STUDENT CODE HERE - VARIABLES DECLARATION
    game_header()
    round = 1

    previous_computer_choice = None
    previous_user_choice = None
    total_computer_score = 0
    total_user_score = 0
    total_computer_xp = 0
    total_user_xp = 0

    while True:
        #STUDENT CODE HERE
        print("Round Number", round)

        # Show the scores only if round is greater than 1
        if round > 1:
            print("Previous Round Result")
            print("=====================")
            print("Previous Computer Choice:", previous_computer_choice)
            print("Previous User Choice:", previous_user_choice)

        previous_user_choice = get_user_choice()
        previous_computer_choice = get_computer_choice()

        print("You picked", previous_user_choice, "and computer", previous_computer_choice)

        winner = determine_winner(previous_user_choice, previous_computer_choice)

        if winner == "player":
            print("Player wins!")
            total_user_score += 1
            total_user_xp += generate_xp(round)

        elif winner == "computer":
            print("Computer wins!")
            total_computer_score += 1
            total_computer_xp += generate_xp(round)

        else:
            print("There's no winner!")

        # Show the Stats after each play
        print("Stats")
        print("=====")
        print("Total Computer Score", total_computer_score)
        print("Total User Score", total_user_score)
        print("Total Computer XP", total_computer_xp)
        print("Total User XP", total_user_xp)
        print()

        prompt = input("Do you want to play another round? (quit to exit game): ").lower()

        if prompt == "quit":
            return

        round += 1


#PREDEFINED
main()