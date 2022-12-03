import random

top_Of_range = input("Type a number: ")

if top_Of_range.isdigit():
    top_Of_range = int(top_Of_range)

    if top_Of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()  


rn = random.randint(0, top_Of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == rn:
        print("You got it!")
        break    
    elif user_guess > rn:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")