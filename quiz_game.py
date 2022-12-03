print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's Play:) ")
score = 0


answer = input(" What does CPU stand For? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input(" What does GPU stand For? ")
if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input(" What does RAM stand For? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input(" What does OS stand For? ")
if answer == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/4) * 100 ) + " %." )