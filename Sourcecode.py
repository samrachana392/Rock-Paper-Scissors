import random

while True:

    item_list=["rock", "paper", "scissors"]
    user_choice = input("Enter your choice(rock, paper, scissors): ").lower()

    if user_choice not in item_list:
        print("Invalid input! Enter again.")
        continue # goes to start of loop

    comp_choice = random.choice(item_list)

    print(f"YOUR CHOICE: {user_choice}")
    print(f"COMPUTER CHOICE: {comp_choice}")

    if(user_choice == comp_choice):
        print("Your choice and computer's choices are same: tie")
    elif user_choice == "rock":
        if(comp_choice=="paper"):
            print("paper covers rock: Computer wins")
        else:
            print("rock smashes scissors: You win")

    elif user_choice == "paper":
        if(comp_choice=="rock"):
            print("paper covers rock: You win")
        else:
            print("scissors cuts paper: Computer wins")

    elif user_choice == "scissors":
            if( comp_choice == "rock"):
                print("rock smashes scissors: computer wins")
            else:
                print("scissors cuts paper: You win")
    else: 
        print("invalid input")
    
    ans = input("Do you want to paly again? (y/n): ").upper()
    if ans != "Y":
        break
