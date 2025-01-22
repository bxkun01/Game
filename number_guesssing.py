import random

print("Welcome to Number Guessing game!")
print("SYSTEM: You only get FIVE lives!")

first_num = int(input("Enter the first number: "))
last_num = int(input("Enter the last number: "))
life = 5
original_num = random.randint(first_num, last_num)

while first_num >= last_num:
    print("You have to enter initial numbers less than last number!")
    first_num = int(input("Enter the first number: "))
    last_num = int(input("Enter the last number: "))

while life:
    guess_num = input("Enter your guess: ")
    
    if not guess_num.isdigit():
        print("Please enter a valid number.")
        continue

    guess_num = int(guess_num)  

    if guess_num == original_num:
        print("System: YOU HAVE WON!!")
        break
    else:
        life -= 1
        print(f"ALERT: WRONG! You have {life} lives left.")
        
    if life == 0:
        print("SYSTEM: YOU LOST!")
        print(f"The number was {original_num}")
