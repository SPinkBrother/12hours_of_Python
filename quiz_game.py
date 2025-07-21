# Introduct
print("Welcome to my quiz game !")

playing = input("Start the game ? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play : ) ")

score = 1
# 
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else: 
    print('Incorrect :(')
    score -= 1

print("You got " + str(score) + "question correct !")