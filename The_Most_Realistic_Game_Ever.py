

print("WELCOME TO THE MOST REALISTIC GAME EVER!!!")
input("Press Enter to start: ")

print("You wake up in the forest")
while True:
    answer1 = input("Enter your next move (climb a tree): ")
    if answer1 == "climb a tree":
        print(f"You {answer1}.\nMore forest. ")
        break
    else:
        print("Try again, you need to climb a tree. ")

while True:
    answer2 = input("Enter your next move (look around): ")
    if answer2 == "look around":
        print(f"You {answer2}.\nYou see more forest. ")
        break
    else:
        print("Try again, you need to look around. ")

while True:
    answer3 = input("Enter your next move (head north): ")
    if answer3 == "head north":
        print(f"You {answer3}.\nYou are in a forest. ")
        print("It's been 30 minutes. Your mother is waiting at the airport. ")
        break
    else:
        print("Try again, you need to head north. ")

while True:
    answer4 = input("Enter your next move (keep heading north): ")
    if answer4 == "keep heading north":
        print("You continue to head north.\nIt has been one hour.\nDusk is falling near the airport. ")
        print("Your mother will be in shadows soon. ")
        break
    else:
        print("Try again, you need to keep heading north. ")

while True:
    answer5 = input("Enter your next move (go out of forest): ")
    if answer5 == "go out of forest":
        print("You are out of the forest. ")
        break
    else:
        print("Try again, you need to go out of the forest. ")

while True:
    answer6 = input("Enter your next move (go to clearing): ")
    if answer6 == "go to clearing":
        print("You are in the clearing.\nYou are no longer in the forest, and therefore the vampires won. ")
        print("The end. ")
        break
    else:
        print("Try again, you need to go to the clearing. ")
