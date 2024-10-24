# Programmers:  Caitlin Burns
# Course:  CS151, Professor Zee
# Due Date: 10/16/24
# Programming Assignment:  PA 2
# Problem Statement:this code lets users play a game of sticks
# Data In: number of sticks, numbers from 1-3, and if users want to play again
# Data Out: total sticks, if users lose, and player 1's choices
# Credits: this code is based on the assignment given in the read me file

import random

#this creates the introduction for the game
def intro():
    print('Sticks is a game where 3 players must select between 1 and 3 sticks from a pre-selected number of sticks. \nPlayer 1 is the computer. The player to select the last stick loses. Good luck!')

#this allows user to choose total sticks
def input_choice():
    total_sticks = int(input('Enter number of sticks (10-100): '))
    while total_sticks < 10 or total_sticks > 100:
        print('Invalid number of sticks')
        total_sticks = int(input('Enter number of sticks (10-100): '))
    print('There are', total_sticks, 'sticks.')
    return total_sticks

#allows player 1 (computer) to go
def p1_turn(total_sticks):
    print('Player 1 selects first')
    p1_choice = random.randint(1, 3)
    print('Player 1 selects', p1_choice)
    total_sticks -= p1_choice
    print(f'There are {total_sticks} sticks.')
    return total_sticks

#allows player 2 to go
def p2_turn(total_sticks):
    p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
    while p2_choice != 1 and p2_choice != 2 and p2_choice != 3:
        print('Invalid choice')
        p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
    print('Player 2 selects', p2_choice)
    total_sticks -= p2_choice
    print(f'There are {total_sticks} sticks.')
    return total_sticks

#allows player 3 to go
def p3_turn(total_sticks):
    p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
    while p3_choice != 1 and p3_choice != 2 and p3_choice != 3:
        print('Invalid choice')
        p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
    print('Player 3 selects', p3_choice)
    total_sticks -= p3_choice
    print(f'There are {total_sticks} sticks.')
    return total_sticks

#exits the loop if there are no more sticks left
def game_over():
    print('Game Over!')

#exits game if user answers no to play again
def exit_game():
    print('Thanks for playing!')

#asks user if they want to play again
def play_again():
    choice =input('Would you like to play again?: ')
    choice = choice.lower()
    while choice != 'no':
        game()
    exit_game()

#puts all the pieces of the game together
def game():
    intro()
    p1_losses = 0
    p2_losses = 0
    p3_losses = 0
    total_sticks = input_choice()
    while total_sticks > 0:
        total_sticks = p1_turn(total_sticks)
        if total_sticks <= 0:
            p1_losses += 1
            game_over()
        elif total_sticks > 0:
            total_sticks = p2_turn(total_sticks)
            if total_sticks <= 0:
                p2_losses += 1
                game_over()
            else:
                total_sticks = p3_turn(total_sticks)
                if total_sticks <= 0:
                    p3_losses += 1
                    game_over()
        else:
            total_sticks = p3_turn(total_sticks)
    game_over()
    print(f'Player 1 has {p1_losses} losses \nPlayer 2 has {p2_losses} losses \nPlayer 3 has {p3_losses} losses')
    play_again()

#sets main program
def main():
    game()

#runs main
main()


