import random

def is_hand(number):
    return number in [0, 1, 2]

def get_player():
    while True:
        try:
            player_choice = int(input("Input your hand\n0: rock, 1: scissors, 2: paper "))
            if is_hand(player_choice):
                return player_choice
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer():
    return random.randint(0, 2)

def get_hand_name(hand_number):
    hands = ['rock', 'scissors', 'paper']
    return hands[hand_number]

def view_hand(player, computer):
    print(f"My hand is {get_hand_name(player)}")
    print(f"Rival’s hand is {get_hand_name(computer)}")

def get_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        return 'win'
    else:
        return 'lose'

# Main game loop
while True:
    print("Start ‘rock-paper-scissors’")
    player_choice = get_player()
    computer_choice = get_computer()
    view_hand(player_choice, computer_choice)

    result = get_result(player_choice, computer_choice)
    print(result)

    if result != 'draw':
        break
