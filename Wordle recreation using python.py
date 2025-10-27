#wordle game with random words
import random

def game():
    global attempts
    guess = input(f"   {"Enter a word: ":>10}").lower()
    if len(guess) !=5:
        print("Enter a 5 letter word.")
        complete()
    else:
        attempts += 1
        for i in range(5):
            guessList[i] = guess[i]
        for i in range(5):
            if guessList[i] == chosenWord[i]:
                blanks[i] = "🟩"
                continue
            elif guessList[i] in chosenWordList:
                blanks[i] = "🟨"
                continue
            elif guessList[i] != chosenWord[i] and guessList[i] not in chosenWordList:
                blanks[i] = "⬛"
                continue
        print(f"{"":^1}", *guessList, sep="   ")
        print(f"{"":^1}", *blanks, sep="  ")
        for i in range(5):
            for j in range(26):
                if guessList[i].lower() == alphabet[j] and guessList[i].lower() == chosenWord[i]:
                    alphabet[j] = alphabet[j].upper()
                    continue
                elif guessList[i].lower() == alphabet[j] and guessList[i] not in chosenWordList:
                    alphabet[j] = "_"
                    continue
                    
            
#display the letters  
        for i in range(13):
            print(alphabet[i], end=" ")
        print()
        print(f"{"":^1}", end="")
        for i in range(13, 26):
            print(alphabet[i], end=" ")
        print()

        complete()

def complete():
    if attempts <6 and guessList != chosenWordList:
        game()
    else:
        for i in range(5):
            blanks[i] = "🟩"
        if guessList == chosenWordList:
            print(f"   {"You Won!":<10}")
        else:
            print(f"   {"Game Over!":>10}")
            print(f"{"":^1}", *chosenWord, sep="   ")
            print(f"{"":^1}", *blanks, sep="  ")

wordList = ["apple", "grape", "pearl", "chair", "table", "flame", "light", "water", "stone", "cloud", "bloom", "dream", "field", "ocean", "river", "storm", "heart", "earth", "green", "plant", "smile", "laugh", "sweet", "sound", "music", "voice", "peace", "angel", "tiger", "zebra", "camel", "eagle", "flock", "swirl", "sword", "blade", "candy", "honey", "juice", "lemon", "mango", "melon", "berry", "bread", "butter", "cheer", "dance", "party", "spark", "shine", "glory", "faith", "trust", "dream", "magic", "ghost", "flour", "grass", "grain", "shade", "night", "light", "daisy", "coral", "shell", "crane", "brick", "block", "plane", "train", "truck", "sugar", "spice", "cream", "apple", "plush", "happy", "crown", "arrow", "beach", "flock", "sweep", "blink", "charm", "frost", "giant", "hound", "mirth", "peach", "queen", "roast", "shark", "storm", "treat", "whale", "world", "youth", "zesty", "vivid", "tiger"]


chosenWord = wordList[random.randint(0, 99)]
chosenWordList = [0] * 5
guessList = [0] * 5
attempts = 0
for i in range(5):
    chosenWordList[i] = chosenWord[i]
blanks = ["⬛"] * 5
blanksWord = ["_"] * 5
print(f"{"":^1}", *blanks, sep="  ")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(f"{"":^1}", end="")
for i in range(13):
    print(alphabet[i], end=" ")
print()
print(f"{"":^1}", end="")
for i in range(13, 26):
    print(alphabet[i], end=" ")
print()
game()

input("Enter to Exit")
#🟨 🟩 ⬛
