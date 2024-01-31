import random

choices = ['rock', 'scissors', 'paper']

while True: 
    player_choice = int(input("Input your hand (0: rock,1: scissors,2:paper):"))
    computer_choice = random.randint(0,2)

    if player_choice == computer_choice:
        result = 'draw'
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2)  or \
         (player_choice == 2 and computer_choice == 0):
        result = 'win'
         
    else:
        result = 'lose' 

        print("start 'rock-paper-scissors' input your hand ")
        print(f"0: {choices[0]}, 1: {choices[1]}, 2: {choices[2]}")
        print(f"My hand is {choices[player_choice]} Computer's hand is {choices[computer_choice]} {result}")

        if result != 'draw':
         break

