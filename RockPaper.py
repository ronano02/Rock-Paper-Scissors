import random

print('''Welcome to Rock, Paper, Scissors!

To Play Just Type Either "Rock", "Paper", or "Scissors".
Or Type "Exit" to Finish Playing.
''')

data = ["Rock", "Paper", "Scissors"]
exit = 0

while exit == 0:
    user = input().lower()
    computer = random.choice(data)
    if user == 'exit':
        exit = 1
    elif user not in {'rock', 'paper', 'scissors'}:
        print("Invalid Entry\n")
    else:
        print(computer)

        computer = computer.lower()
        if user == computer:
            print("Tie\n")
        elif (user == "rock" and computer == "scissors") or (user == "scissor" and computer == "paper") \
        or (user == "paper" and computer == "rock"):
            print("You Win!\n")
        else:
            print("You Lose!\n")





