hands = ['rock', 'scissors','paper']

while True:
     user_input = input('0: rock, 1: scissors, 2 paper(press q to quit):')

     if user_input == 'q':
          break
index = int(user_input) if user_input.isdigit() else -1
hand = hands[index] if 0 <= index <=2 else None

if hand: 
     print(f"you selected: {hand}")
else: 
     print("Invalid input. please enter a number between 0 and 2.")