import random


def play_game():
    rand_num = random.randint(1,51)
    guesses = 6

    border = "=" * 78
    print(border)
    print(" NUMBER GUESSING GAME ".center(78))
    print(" Guess a number from 1-50".center(78))
    print(border)
    while guesses > 0:
        print(f"\n Guesses Left: {guesses}")
        try:
            user = int(input(" Enter your guess: "))
        except ValueError:
            print("Enter a valid number")
            continue
        print(border)

        if user < rand_num:
            print("Too low! Try again.\n")
            guesses -= 1

        elif user > rand_num:
            print("Too high! Try again.\n")
            guesses -= 1

        else:
            print("Woah! You guessed the correct number! You won!")
            print(border)
            return True

    if guesses == 0:
        print(f"You ran out of guesses! The correct answer was {rand_num}.")
        print(border)
        return False
streak = 0 

while True:
    won = play_game()
    if won:
        streak += 1
        print(f"Current Winning Streak: 🔥{streak}")
    else:
        streak = 0
        print(f"Winning Streak Reseted to: 🔥{streak}")

    replay = input("\nDo you wanna play again, y/n: ")
    if replay == "n":
        print("\nThank you for playing!")
        break
    elif replay != "y":
        print("Invaild input, exiting.....")
        break



