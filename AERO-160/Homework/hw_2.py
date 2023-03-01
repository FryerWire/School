
"""
Homework 2 - Rock, Paper, Scissors
Maxwell Seery
"""

import random

ATTACK_OPTIONS = ["rock", "paper", "scissors"]

print("\nWelcome to 'Rock, Paper, Scissors'!\n")

def play_game(attempts):
    """
    Asks the user to enter either 'Rock', 'Paper', or 'Scissors'. The program then checks whether or not the 
    user has beaten the computer in each of three rounds.

    Parameters
        - attempts (int) : Outside of the play_game function, the while loop adds up a each attempt and sends it to this function
    
    Returns
        - user_win (int)     : Returns the number of wins the player has won
        - computer_win (int) : Returns the number of wins the computer has won
    """

    computer_win = 0                                                                                                # Score of computer wins
    user_win = 0                                                                                                    # Score of user wins

    if not (attempts > 3):                                                                                          # if attempts isn't over 3
        print(f"\nAttempt: {attempts}/3")                                                                           # print each of the attempts

    computer_choice = random.choice(ATTACK_OPTIONS)                                                                 # computer randomly chooses an option

    while True:                                                                                                     # while loop to check for user input
        user_choice = str(input("Please enter either 'Rock', 'Paper', or 'Scissors': ")).lower()                    # User enters only a string for an attack option
        if ((type(user_choice) != str) or (user_choice not in ATTACK_OPTIONS)):                                     # parameters to check data input
            print("\nERROR: ")                                                                                      # prints an error and then starts the loop over
            continue                                                                                                # continues the loop
        else:
            break                                                                                                   # breaks out of the loop

    if (user_choice == computer_choice):                                                                            # checks if the user and computer are tied
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"The computer chose: {computer_choice.capitalize()}")
        print("Tie!\n")

    elif (user_choice == 'rock') and (computer_choice == 'scissors'):                                               # Game option checks
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"The computer chose: {computer_choice.capitalize()}")
        print("You won!\n")
        user_win += 1                                                                                               # Adds a point for the user winning

    elif (user_choice == 'paper') and (computer_choice == 'rock'):                                                  # Game option checks
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"The computer chose: {computer_choice.capitalize()}")
        print("You won!\n")
        user_win += 1                                                                                               # Adds a point for the user winning

    elif (user_choice == 'scissors') and (computer_choice == 'paper'):                                              # Game option checks
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"The computer chose: {computer_choice.capitalize()}")
        print("You won!\n")
        user_win += 1                                                                                               # Adds a point for the user winning

    else:
        print(f"\nYou chose: {user_choice.capitalize()}")                                                           # If the user didn't win above the computer wins
        print(f"The computer chose: {computer_choice.capitalize()}")
        print("You lost!\n")
        computer_win += 1                                                                                           # Adds a point for the computer winning

    return user_win, computer_win                                                                                   # Returns the score for each round played

user_wins = 0                                                                                                       # User wins starts at zero
computer_wins = 0                                                                                                   # Computer wins starts at zero
play_count = 1                                                                                                      # Play count is what determins the game attempts count
another_round = True                                                                                                # Another round determinds if the while loop will run again
while another_round:                                                                                                # Another round is set to True making the loop run again
    user_win, computer_win = play_game(play_count)                                                                  # Calls the play_game function with a parameter of play_count
    user_wins += user_win                                                                                           # Adds the user wins score to the global variable
    computer_wins += computer_win                                                                                   # Adds the computer wins score to the global variable

    if (play_count == 3):                                                                                           # If the play count has reached 3
        if (user_wins == computer_wins):                                                                            # Checks for a tied game
            print(f"\nUser total points: {user_wins}")
            print(f"Computer total points: {computer_wins}")
            print("It's a tied game!")                                                                     

        elif (user_wins > computer_wins):                                                                           # Checks if the user won
            print(f"\nUser total points: {user_wins}")
            print(f"Computer total points: {computer_wins}")
            print(f"You won by {user_wins - computer_wins} points")
        
        else:
            print(f"\nUser total points: {user_wins}")                                                              # Checks if the computer won
            print(f"Computer total points: {computer_wins}")
            print(f"You lost by {computer_wins - user_wins} points")

        while True:                                                                                                 # While loop to check for data input correctness
            play_again_options = ['yes', 'no']                                                                      # Play game again options
            play_again = str(input("\nDo you want to play another three rounds? ('Yes' or 'No'): ")).lower()        # User input for more rounds
            if (type(play_again) != str) or (play_again not in play_again_options):                                 # Checks if the user typed the input correctly
                print("\nERROR: Please enter either 'Yes' or 'No' please.")                                         # Prints an ERROR message
                continue                                                                                            # Runs the loop again for correct information
            elif (play_again == "no"):                                                                              # If chosen 'No' then the game will quit
                print("\nThank you for playing 'Rock, Paper, Scissors'!")                                           # Thank you message
                another_round = False                                                                               # Makes the main loop False and then it stops running
                break                                                                                               # Breaks out of local loop
            else:
                user_wins = 0                                                                                       # Score resets
                computer_wins = 0
                play_count = 0
                break                                                                                               # Breaks out of local loop

    play_count += 1                                                                                                 # Adds to the global variable for record keeping


