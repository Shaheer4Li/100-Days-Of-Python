import random
print(''' ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░  ''')
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#declarations and and word bank
word_bank = [
    "apple", "river", "mountain", "computer", "keyboard", "ocean", "forest", "city", "village", "car",
    "train", "airplane", "school", "teacher", "student", "book", "pencil", "phone", "camera", "bottle",
    "window", "door", "garden", "flower", "tree", "cloud", "rain", "storm", "sun", "moon",
    "star", "planet", "galaxy", "universe", "island", "beach", "desert", "valley", "hill", "bridge",
    "road", "street", "building", "house", "castle", "tower", "ship", "boat", "harbor", "market",
    "shop", "restaurant", "hotel", "office", "factory", "hospital", "library", "museum", "park", "stadium",
    "ball", "game", "team", "player", "coach", "doctor", "nurse", "artist", "writer", "poet",
    "song", "music", "movie", "picture", "painting", "statue", "engine", "machine", "robot", "device",
    "battery", "screen", "speaker", "microphone", "clock", "watch", "wallet", "bag", "shoe", "shirt",
    "jacket", "hat", "ring", "necklace", "bracelet", "table", "chair", "sofa", "bed", "pillow",
    "blanket", "plate", "cup", "spoon", "fork", "knife", "bowl", "lamp", "mirror", "carpet",
    "box", "gift", "letter", "paper", "notebook", "folder", "file", "document", "map", "ticket",
    "passport", "key", "lock", "chain", "rope", "ladder", "hammer", "nail", "screw", "tool",
    "weapon", "shield", "helmet", "armor", "crown", "flag", "coin", "money", "bank", "credit",
    "account", "card", "code", "password", "signal", "network", "server", "database", "program", "software",
    "virus", "system", "memory", "data", "algorithm", "formula", "theory", "law", "rule", "policy",
    "agreement", "contract", "plan", "project", "task", "goal", "dream", "idea", "thought", "mind",
    "brain", "heart", "soul", "voice", "sound", "light", "shadow", "fire", "smoke", "ice",
    "energy", "power", "force", "speed", "time", "history", "future", "moment", "chance", "luck"
]
lisht =[]
lives = 6
#choosing Selected_word from available
Selected_word = random.choice(word_bank)
#Creating list of dashes 
for i in range(len(Selected_word)):
    lisht.append("_")
#on/off variable for game
game_over = False
#core loop of game 
while not game_over:
    #printing initial list so that player can get idea about number of words to guess
    for i in lisht:
         print(i, end=" ")
    #printing hangman figures on every loop
    print(HANGMANPICS[6-lives])
    #taking user input
    Guess = input("Please Enter you guess  ").lower()
    #checking if added character is already guessed or not and awaring player about it
    for i in lisht:
        if i == Guess:
            print("you've already entered that character")
    #checking if our guessed letter is in word or not if yes then change corresponding dashes in lisht to this character
    for i in range(len(Selected_word)):
        
        if Selected_word[i] == Guess:
            lisht[i] = Guess
    #if guessed character is wrong then -1 lives and aware the player
    if Guess not in Selected_word:
        lives-=1
        print("oops you've made a mistake lives = -01")
        #both game over conditions win or lose
    if lives == 0:
        game_over = True
        print(f"you lost correct word is : {Selected_word}")
    elif "_" not in lisht:
        game_over = True  
        print("you guessed it right")      
     

