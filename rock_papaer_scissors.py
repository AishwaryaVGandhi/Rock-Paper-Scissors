import random

rock_paper_scissors = ["✊","🖐","✌️"]

print("Type 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n")
user = int(input("Enter your choice : "))

if user > 2 or user < 0:
    print("\nInvalid Choice, Computer Won !!")
else:
    print("\nYou : ", rock_paper_scissors[user])
    computer = random.randint(0,2)
    print("computer : ", rock_paper_scissors[computer])
    
    if computer == user:
        print("\nIt's a Draw !!")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("\nYou Won !!")
    else:
        print("\nComputer Won !!")
