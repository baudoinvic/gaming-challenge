
def get_hand_name(hand_number):
    hands = ['rock', 'scissors', 'paper']
    return hands[hand_number]

def view_hand(player, computer):
    print(f"My hand is: {get_hand_name(player)}")
    print(f"Computer's hand is: {get_hand_name(computer)}")

player_choice = 0
computer_choice = 2

view_hand(player_choice, computer_choice)