import random
import string

data = {}

print("Guess the computer's choice to win the prize")

a = [1, 2, 3, 4, 5, 6, 7]

while True:
    username = input("Username:> ")
    trial = 3
    score = 0

    while trial > 0:
        random.shuffle(a)
        print("Select a number from", a)
        com_choice = random.choice(a)
        user = int(input("Your choice:> "))
        if user == com_choice:
            print("YOU WIN")
            score += 2
            trial += 1
            print(f"YOU HAVE WON AN EXTRA TRIAL")
            print(f"{trial} trial(s) left")
        else:
            if user > com_choice:
                print("TOO HIGH")

            else:
                print("TOO LOW")
            trial -= 1
            print(f"{trial} trial(s) left")
    prev_score = data.get(username, 0)
    if score > prev_score:
        print("You just beat your prevous high score! 🎉🎉🎉")
        data[username] = score

    print(f"You scored {score} points")
    print("Game Over ): ")

    choice = input("Play again? Y/N").lower()
    if choice == "n":
        break

print(data)
