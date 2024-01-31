import random

print ('Rock-paper-Scissors Game')
choices = ['rock', 'scissors','paper']

player_choice = random.randint(0, 2)

computer_choice = random.randint(0,2)

print('Player\'s choice:', choices[player_choice])
print('Computer\'s choice:', choices[computer_choice])

#the outcome

if player_choice == computer_choice:
    print("It's a draw")
elif (player_choice == 0 and computer_choice == 1) or \
     (player_choice == 1 and computer_choice == 2) or \
     (player_choice == 2 and computer_choice == 0):
      print("Player wins")
else: 
      print("Computer wins") 