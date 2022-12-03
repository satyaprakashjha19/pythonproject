import random

user_wins = 0
comp_wins = 0

Option = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in Option:
        continue

    rn = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    comp_pick = Option[rn]
    print("comp_pick", comp_pick + ".")


    if user_input == "rock" and comp_pick == "scissors":
        print("You win!")
        user_wins+= 1

    elif user_input == "paper" and comp_pick == "rock":
        print("You win!")
        user_wins+= 1
        
    elif user_input == "scissors" and comp_pick == "paper":
        print("You win!")
        user_wins+= 1
    else:
        print("You Lost!")
        comp_wins += 1

print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
print("Goodbye")