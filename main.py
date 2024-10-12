# Code goes here and DO NOT FORGET INTRO COMMENTS
import random

#this code creates a game of sticks between 3 players. the player to select the last stick loses

print('Sticks is a game where 3 players must select between 1 and 3 sticks from a pre-selected number of sticks. Player 1 is the computer. The player to select the last stick loses. Good luck!')
total_sticks = int(input('Enter number of sticks (10-100): '))
while total_sticks < 10 or total_sticks > 100:
    print('Invalid number of sticks')
    total_sticks = int(input('Enter number of sticks (10-100): '))
print('There are', total_sticks, 'sticks.')



print('Player 1 selects first')
p1_choice = random.randint(1, 3)
print('Player 1 selects', p1_choice)
updated_sticks = (total_sticks - p1_choice)
updated_sticks = int(updated_sticks)
p1_updated = updated_sticks
p1_updated = int(p1_updated)
if p1_updated == 0:
    p1_losses = 1
else:
    p1_losses = 0


p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
while p2_choice != 1 and p2_choice != 2 and p2_choice != 3:
    print('Invalid choice')
    p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
print('Player 2 selects', p2_choice)
updated_sticks = (updated_sticks - p2_choice)
updated_sticks = int(updated_sticks)
p2_updated = updated_sticks
p2_updated = int(p2_updated)
if p2_updated == 0:
    p2_losses = 1
else:
    p2_losses = 0


p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
while p3_choice != 1 and p3_choice != 2 and p3_choice != 3:
    print('Invalid choice')
    p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
print('Player 3 selects', p3_choice)
updated_sticks = (updated_sticks - p3_choice)
updated_sticks = int(updated_sticks)
p3_updated = updated_sticks
p3_updated = int(p3_updated)
if p3_updated == 0:
    p3_losses = 1
else:
    p3_losses = 0

SENTINEL = 0
while updated_sticks != SENTINEL:
    p1_choice = random.randint(1, 3)
    print('Player 1 selects', p1_choice)
    updated_sticks = (updated_sticks - p1_choice)
    updated_sticks = int(updated_sticks)
    p1_updated = updated_sticks
    p1_updated = int(p1_updated)
    p1_losses = 0
    if p1_updated == 0:
     p1_losses = 1 + p1_losses
    else:
        p1_losses = 0 + p1_losses
    p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
    while p2_choice != 1 and p2_choice != 2 and p2_choice != 3:
        print('Invalid choice')
        p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
    print('Player 2 selects', p2_choice)
    updated_sticks = (updated_sticks - p2_choice)
    updated_sticks = int(updated_sticks)
    updated_sticks = updated_sticks
    p2_updated = updated_sticks
    p2_updated = int(p2_updated)
    p2_losses = 0
    if p2_updated == 0:
        p2_losses = 1 + p2_losses
    else:
        p2_losses = 0 + p2_losses

    p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
    while p3_choice != 1 and p3_choice != 2 and p3_choice != 3:
        print('Invalid choice')
        p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
    print('Player 3 selects', p3_choice)
    updated_sticks = (updated_sticks - p3_choice)
    updated_sticks = int(updated_sticks)
    p3_updated = updated_sticks
    p3_updated = int(p3_updated)
    p3_losses = 0
    if p3_updated == 0:
        p3_losses = 1 + p3_losses
    else:
        p3_losses = 0 + p3_losses
print('Game over')
play_again = input('Would you like to play again? (y/n): ')
SENTINEL = 'n'
while play_again != SENTINEL:
    total_sticks = int(input('Enter number of sticks (10-100): '))
    while total_sticks < 10 or total_sticks > 100:
        print('Invalid number of sticks')
        total_sticks = int(input('Enter number of sticks (10-100): '))
    print('There are', total_sticks, 'sticks.')

    print('Player 1 selects first')
    p1_choice = random.randint(1, 3)
    print('Player 1 selects', p1_choice)
    updated_sticks = (total_sticks - p1_choice)
    updated_sticks = int(updated_sticks)
    p1_updated = updated_sticks
    p1_updated = int(p1_updated)
    if p1_updated == 0:
        p1_losses = 1
    else:
        p1_losses = 0

    p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
    while p2_choice != 1 and p2_choice != 2 and p2_choice != 3:
        print('Invalid choice')
        p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
    print('Player 2 selects', p2_choice)
    updated_sticks = (updated_sticks - p2_choice)
    updated_sticks = int(updated_sticks)
    p2_updated = updated_sticks
    p2_updated = int(p2_updated)
    if p2_updated == 0:
        p2_losses = 1
    else:
        p2_losses = 0

    p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
    while p3_choice != 1 and p3_choice != 2 and p3_choice != 3:
        print('Invalid choice')
        p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
    print('Player 3 selects', p3_choice)
    updated_sticks = (updated_sticks - p3_choice)
    updated_sticks = int(updated_sticks)
    p3_updated = updated_sticks
    p3_updated = int(p3_updated)
    if p3_updated == 0:
        p3_losses = 1
    else:
        p3_losses = 0

    SENTINEL = 0
    while updated_sticks != SENTINEL:
        p1_choice = random.randint(1, 3)
        print('Player 1 selects', p1_choice)
        updated_sticks = (updated_sticks - p1_choice)
        updated_sticks = int(updated_sticks)
        p1_updated = updated_sticks
        p1_updated = int(p1_updated)
        p1_losses = 0
        if p1_updated == 0:
            p1_losses = 1 + p1_losses
        else:
            p1_losses = 0 + p1_losses
        p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
        while p2_choice != 1 and p2_choice != 2 and p2_choice != 3:
            print('Invalid choice')
            p2_choice = int(input('Player 2 selects next. 1, 2, or 3?: '))
        print('Player 2 selects', p2_choice)
        updated_sticks = (updated_sticks - p2_choice)
        updated_sticks = int(updated_sticks)
        updated_sticks = updated_sticks
        p2_updated = updated_sticks
        p2_updated = int(p2_updated)
        p2_losses = 0
        if p2_updated == 0:
            p2_losses = 1 + p2_losses
        else:
            p2_losses = 0 + p2_losses

        p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
        while p3_choice != 1 and p3_choice != 2 and p3_choice != 3:
            print('Invalid choice')
            p3_choice = int(input('Player 3 selects next. 1, 2, or 3?: '))
        print('Player 3 selects', p3_choice)
        updated_sticks = (updated_sticks - p3_choice)
        updated_sticks = int(updated_sticks)
        p3_updated = updated_sticks
        p3_updated = int(p3_updated)
        p3_losses = 0
        if p3_updated == 0:
            p3_losses = 1 + p3_losses
        else:
            p3_losses = 0 + p3_losses
    print('Game over')
    play_again = input('Would you like to play again? (y/n): ')
print('Thank you for playing.')
print('The final score was: \nPlayer 1:', p1_losses, 'losses \nPlayer 2:', p2_losses, 'losses \nPlayer 3:', p3_losses,'losses')





