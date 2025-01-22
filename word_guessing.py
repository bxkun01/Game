import random

words=['heaven', 'immortality', 'pain', 'demon',
        'righteous','dream','ultra','peekaboo'
]



def play():
    original_word = random.choice(words).lower()
    life= 5
    print(f"Welcome to word guessing game!\nYou need to guess a single word from the given:")
    for word in words:
        print(f"  -{word}")

    while life>0:
        guess= input("Guess: ").lower()
        if guess not in words:
            print("You need to select word from the list only!!")
            print("[Restarting the game]")
            for word in words:
                print(f"  -{word}")
            continue
            
        if guess == original_word:
            print("You have won!")
            break
        else:
            life-=1
            print(f"Try again! {life} lives remaining")
            continue

    if life==0:
        print("[Game Over!]")
        print(f"The word was {original_word.upper()}")
        replay= input("Do you wanna play again?\nPress 'Y'to play again and 'N' to exit: ").strip().upper()
        if replay=='Y':
            play()
        else:
            print("Exiting the game!")


play()







