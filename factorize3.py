import random

def start_message():
    print("Welcome to rock-paper-Scissors game")
def get_player():
      return int(input("Enter your choice (0 for rock, 1 for scissors, 2 for paper): "))
def get_computer():
     return random.randint(0,2)
def view_result(hand_diff):
     outcomes = ["it's a draw", "player wins", "computer wins"]
     print(outcomes[hand_diff])

def main():
     start_message()
     player_choice = get_player()
     computer_choice = get_computer()
     hand_diff = (player_choice - computer_choice) % 3
     view_result(hand_diff)

if __name__ == "__main__":
    main()