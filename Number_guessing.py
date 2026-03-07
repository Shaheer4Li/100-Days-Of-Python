import random
lives = 0 
print(r'''
 _   _                 _                 _____                     _              
| \ | |               | |               |  __ \                   (_)             
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | 
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | 
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, | 
                                                                            __/ | 
                                                                           |___/   ''')
easy_or_hard = input("Which mode do you want Easy🤡 or hard 🥵 :  ").lower()
if easy_or_hard == "easy":
    lives = 10
else:
    lives = 5
def main(guesses):
    
    print("============= Guess The number between 1 and 100")
    runner = True

    number = random.randrange(0,101)
    while runner:
        if guesses <= 0:
            print("You ran out of lives💥")
            return
        print(f"you Have {guesses} guesses left")
        guess = int(input("Make your guess =   "))        
        if guess == number:
            print(f"You Guessed it right number is {number} 😁")
            return
        elif guess < number:
            print("too low 💔\n")
            guesses -= 1
        else:
            print("too high💔 \n")
            guesses -=1
main(lives)

