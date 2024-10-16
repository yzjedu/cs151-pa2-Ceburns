# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

1. import the random module from python
2. output an introduction explaining the game and that player 1 will be the computer
3. create a total sticks variable for the user to enter a number of sticks between 10 and 100
4. while total sticks is less than 10 and greater than 100
   1. output invalid number
   2. ask user to enter a number between 10 and 100
5. output the total number of sticks
6. output player 1 selects first
7. set a player 1 choice variable equal to a random int between 1 and 3
8. output player 1 choice
9. set total sticks to total sticks minus player 1 choice and output total
11. if player 1 total is equal to 0
    1. player 1 losses is equal to 1
12. otherwise
    1. player 1 losses is equal to 0
13. set a player 2 choice variable and have user input 1, 2, or 3 
14. while player 2 choice is not equal to 1, 2, or 3
    1. output invalid choice
    2. ask user to enter 1, 2, or 3
15. output player 2 selection
16. set total sticks as total minus player 2 choice and output total sticks
18. if player 2 total is equal to 0
    1. player 2 losses is equal to 1
19. otherwise
    1. player 2 losses is equal to 0
20. set a player 3 choice variable and have user input 1, 2, or 3
21. while player 3 choice is not equal to 1, 2, or 3
    1. output invalid choice
    2. ask user to enter 1, 2, or 3
22. output player 3 selection
23. set total as total minus player 3 choice
25. if player 3 total is equal to 0
    1. player 3 losses is equal to 1
26. otherwise
    1. player 3 losses is equal to zero
27. set SENTINEL equal to 0
28. while updated sticks is not equal to SENTINEL
    1. output player 1 selects first
    2. set a player 1 choice variable equal to a random int between 1 and 3
    3. output player 1 choice
    4. set total equal to total minus player 1 choice and output total
    6. if player 1 total is equal to 0
        1. player 1 losses is equal to 1 + player 1 losses variable
    7. otherwise
        1. player 1 losses is equal to 0 + player 1 losses variable
    8. set a player 2 choice variable and have user input 1, 2, or 3 
    9. while player 2 choice is not equal to 1, 2, or 3
        1. output invalid choice
        2. ask user to enter 1, 2, or 3
    10. output player 2 selection
    11. set total equal to sticks minus player 2 choice and output total
    13. if player 2 total is equal to 0
        1. player 2 losses is equal to 1 + player 2 losses variable
    14. otherwise
        1. player 2 losses is equal to 0 + player 2 losses variable
    15. set a player 3 choice variable and have user input 1, 2, or 3
    16. while player 3 choice is not equal to 1, 2, or 3
        1. output invalid choice
        2. ask user to enter 1, 2, or 3
    17. output player 3 selection
    18. set total equal to total sticks minus player 3 choice and output total
    20. if player 3 total is equal to 0
        1. player 3 losses is equal to 1 + player 3 losses variable
    21. otherwise
        1. player 3 losses is equal to zero + player 3 losses variable
29. output game over
30. ask user if they would like to play again and store answer in a variable
31. set SENTINEL equal to no
32. while play again variable is not equal to SENTINEL
    1. loop entire code again
33. output thank you for playing
34. output total losses for each player