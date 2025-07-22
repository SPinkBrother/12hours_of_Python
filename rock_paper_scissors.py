import random

user_wins = 0
computer_win = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input =  input("Type Rock/Paper/Scissors or Q to quit. \n").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Please input the correct input !")
        break
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer pick ",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost !")
        computer_win += 1

print("Your score: " , user_wins, "times.")
print("Computer score: " , computer_win, "times.")
print("Goodbye !")