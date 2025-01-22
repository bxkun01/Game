import random

options= ['rock','paper','scissor']
computer_choice= random.choice(options)
win,loss,draw = 0,0,0

print("Welcome to Rock, Paper and Scissor game!")
print("Press 'q' to exit the game")

while True:
    user_choice= input("Enter your choice: ").lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        if win or loss !=0:
            print()
            print("Your score are: ")
            print(f'Win={win}\nLoss={loss}\ndraw={draw}')
        break

    if user_choice not in options:
        print("Invalid! You need to choose rock, paper or scissor!")
        continue


    if user_choice == computer_choice:
        print("Its a draw!")

        draw+=1
    elif (user_choice=='rock' and computer_choice=='scissor') or (user_choice=='rock' and computer_choice=='paper'):
        print("You won!")
        win+=1
    else:
        print("You lost!")
        loss+=1



