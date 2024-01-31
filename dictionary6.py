
choices = ['rock', 'scissors', 'paper']
player_choice = 1  
computer_choice = 2 

if player_choice == computer_choice:
    result = 'draw'
elif (player_choice == 0 and computer_choice == 1) or \
     (player_choice == 1 and computer_choice == 2) or \
     (player_choice == 2 and computer_choice == 0):
    result = 'win'
else:
    result = 'lose'

print("Start 'rock-paper-scissors' Input your hand")
print(f"0: {choices[0]}, 1: {choices[1]}, 2: {choices[2]}")
print(f"My hand is {choices[player_choice]} Computer's hand is {choices[computer_choice]} {result}")
