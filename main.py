# Programmers:  Caitlin Burns
# Course:  CS151, Professor Zee
# Due Date: 10/16/24
# Programming Assignment:  PA 4
# Problem Statement:this code lets users play a game of sticks
# Data In: number of sticks, numbers from 1-3, and if users want to play again
# Data Out: total sticks, if users lose, and player 1's choices
# Credits: this code is based on the assignment given in the read me file

import random

#this code creates a game of sticks between 3 players. the player to select the last stick loses

#this sets the guidelines for the game
print('Sticks is a game where 3 players must select between 1 and 3 sticks from a pre-selected number of sticks. \nPlayer 1 is the computer. The player to select the last stick loses. Good luck!')
total_sticks = int(input('Enter number of sticks (10-100): '))
while total_sticks < 10 or total_sticks > 100:
    print('Invalid number of sticks')
    total_sticks = int(input('Enter number of sticks (10-100): '))
print('There are', total_sticks, 'sticks.')


print('Player 1 selects first')
p1_choice = random.randint(1, 3)
print('Player 1 selects', p1_choice)
total_sticks -= p1_choice
print(f'There are {total_sticks} sticks.')

#this allows player 2 to go
p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
while p2_choice != 1 and p2_choice != 2 and p2_choice != 3:
    print('Invalid choice')
    p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
print('Player 2 selects', p2_choice)
total_sticks -= p2_choice
print(f'There are {total_sticks} sticks.')

#this allows player 3 to go
p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
while p3_choice != 1 and p3_choice != 2 and p3_choice != 3:
    print('Invalid choice')
    p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
print('Player 3 selects', p3_choice)
total_sticks -= p3_choice
print(f'There are {total_sticks} sticks.')

