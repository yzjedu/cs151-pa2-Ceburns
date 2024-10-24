# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 


* purpose: output introduction
* name: intro
* parameter: none
* return: none
* Algorithm:
  1.   output a statement explaining the game of sticks


* purpose: allows user to select amount of sticks
* name: input choice
* parameter: none
* return: total sticks
* algorithm:
  1. prompt user to input a number between 10-100 and set answer equal to variable called total sticks 
     1. if input is not 10-100
        2. output invalid number
        3. ask user to input again
  2. output the total sticks
  3. return total sticks


* purpose: allows player 1 to go
* name: p1 turn
* parameter: total sticks
* return: total sticks
* algorithm:
  1. output player 1 selects first
  2. assign p1 choice variable to a random integer choice between 1 and 3
  3. output p1 choice
  4. subtract p1 choice from total sticks and save it as total sticks
  5. output total sticks
  6. return total sticks


* purpose: allows player 2 to go
* name: p2 turn
* parameter: total sticks
* return: total sticks
* algorithm:
  1. ask user to input 1, 2, or 3 and assign input to variable p2 choice
  2. while p2 choice is not equal to 1, 2, or 3
     1. output invalid choice
     2. ask user to input again
  3. output p2 choice
  4. subtract p2 choice from total sticks
  5. output total sticks
  6. return total sticks


* purpose: allows player 3 to go
* name: p3 turn
* parameter: total sticks
* return: total sticks
* algorithm:
  1. ask user to input 1, 2, or 3 and assign input to variable p2 choice
  2. while p3 choice is not equal to 1, 2, or 3
     1. output invalid choice
     2. ask user to input again
  3. output p3 choice
  4. subtract p3 choice from total sticks
  5. output total sticks
  6. return total sticks


* purpose: displays message when game ends
* name: game over
* parameter: none
* return: none
* algorithm:
    1. output game over


* purpose: exits game
* name: exit game
* parameter: none
* return:none
* algorithm:
    1. output 'Thanks for playing'


* purpose: allows user to play again
* name: play again
* parameter: none
* return: none
* algorithm:
    1. ask user if they want to play again and assign answer to choice variable
  2. convert choice to lowercase
  3. while choice is not equal to no
     1. call game function
  4. call exit game function


* purpose: puts the whole game together
* name: game
* parameter: none
* return: none
* algorithm:
    1. call intro function
  2. create variable for p1 losses, p2 losses, and p3 losses
  3. set total sticks equal to input choice function
  4. while total sticks is greater than 0
     1. total sticks is equal to p1 turn function
     2. if total sticks is less than or equal to 0
        1. p1 losses plus equals 1
        2. call game over function
     3. otherwise if total sticks is greater than 0
        1. total sticks equal p2 turn function
        2. if total sticks is less than or equal to zero
           1. p2 losses plus equals 1
           2. call game over function
        3. otherwise 
           1. total sticks is equal to p3 turn function
           2. if total sticks is less than or equal to 0
              1. p3 losses plus equals 1
              2. call game over function
     4. otherwise
        1. total sticks is equal to p3 turn function
  5. call game over function
  6. output total player losses
  7. call play again function


* purpose: run main program
* name:main
* parameter: none
* return: none
* algorithm:
  1. call game function


1. run main function
    