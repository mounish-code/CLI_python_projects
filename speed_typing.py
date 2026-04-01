import random
import time

def play_game():
    sentence = [
        "Please take your dog, Cali, out for a walk? he really needs some exercise!",
        "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
        "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
        "Do you know why all those chemicals are so hazardous to the environment?",
        "You never did tell me how many copper pennies were in that jar; how come?",
        "Max Joykner sneakily drove his car around every corner looking for his dog.",
        "The two boys collected twigs outside, for over an hour, in the freezing cold!",
        "When do you think they will get back from their adventure in Cairo, Egypt?",
        "Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.",
        "Hector quizzed Mr. Vexife for two hours, but he was unable to get any information."
    ]

    selected_sent = random.choice(sentence)

    border = "=" * 78
    print(border)
    print("TEST YOUR TYPING SPEED".center(78))
    print(border)

    resp = input("Are you ready y/n: ").lower()
    if resp in ["y", "yes"]:
        print("Your sentence:")
        print(selected_sent)

        start =  time.time()
        user = input("type here -> ")
        end = time.time()

        correct = 0
        original_words = selected_sent.split()
        user_words = user.split()
        for i in range(len(original_words)):
            if i < len(user_words):
                if original_words[i] == user_words[i]:
                    correct += 1
        
        elapsed = end - start
        minutes = elapsed / 60
        wpm = (len(user) / 5) / minutes if minutes > 0 else 0
        accuracy = (correct / len(original_words)) * 100 if original_words else 0
        print(border)
        print(f"""{'GREAT WORK!'.center(78)}
        Stats:  
        WPM = {wpm:.0f}
        ACCURACY = {accuracy:.0f}%
        TIME TAKEN = {elapsed:.0f}secs""")
        print(border)
        
    else:
        print("Enter valid characters")

play_game()

while True:
    replay = input("\nDo you wanna play again? y/n: ").lower()
    if replay in ["y", "yes"]:
        play_game()
    elif replay in ["n", "no"]:
        print("Thanks for playing!")
        break
    else:
        print("please enter y or no")