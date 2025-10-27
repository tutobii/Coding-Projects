#Goal: make a hanged man game.
import random

#functions for the game
def guess(userGuess):
    global attempts
    if userGuess.lower() == "clue":
        print("Clue:", wordList[selectedWord])
        print(*blanks, sep=" ")
        complete()
    elif len(userGuess) != 1:
        print("Enter only 1 letter.")
        print(*blanks, sep=" ")
        complete()
    if attempts != 6:
        if userGuess.lower() in lowercase:
            for i in range(len(selectedWord)):
                if userGuess.lower() == lowercase[i]:
                    blanks[i] = selectedWord[i]
                else:
                    continue
            print("There is", userGuess, "in the word")
            print(*blanks, sep=" ")
            complete()
        elif blanks != Theword and userGuess.lower() != "clue" and userGuess.lower() not in lowercase:
            print("No", userGuess, "in the word")
            print(*blanks, sep=" ")
            attempts += 1
            complete()
    else:
        complete()

# check if complete    
def complete():
    if blanks == Theword:
        print("Game Over. You Won!")
    elif blanks != Theword and attempts == 6:
        print("Game Over. You Lost!")
        print("The word is", selectedWord)
    else:
        guess(input("Enter a letter: "))

#Dictionary and word index
wordList = {
    "Boolean": "A fundamental data type that is critical for decision-making by allowing programs to choose between different paths based on conditions",
    "if else Statement": "A primary decision structure that guides a program to take different actions depending on whether a specified requirement is deemed true or false",
    "elif Statement": "A construct used to evaluate several possibilities sequentially when more than two conditions need to be tested",
    "Nested if statement": "The placement of one condition check inside another, generally used when evaluating multiple related conditions in sequence",
    "for Loop": "A repeating control structure designed to execute a block of code for every item contained within a sequence",
    "while Loop": "A control structure that continues to repeat a block of code only as long as a particular condition maintains a true status",
    "break Statement": "A command used within a repeating structure to halt its execution immediately, causing the program to continue afterward",
    "continue Statement": "A command used within a repeating structure to skip the remaining code for the current cycle and proceed immediately to the next cycle",
    "Python Functions": "A defined block of statements intended to perform a specific task, primarily to group repeated tasks for code reuse",
    "def keyword": "The reserved word used to signal the beginning of a user-defined block of reusable statements",
    "Class": "A user-defined template for creating objects, which bundles data and functions together into a single unit",
    "Object": "A specific instance created from a template that holds its own set of unique properties and can utilize the template's defined methods",
    "__init__() Function": "A special method in a class that automatically handles the initial setup of data properties when a new instance of the class is brought into existence",
    "Self Parameter": "A reference necessary within a class to access the attributes and methods belonging to the specific current instance",
    "Inheritance": "A principle that allows one template type (class) to acquire the capabilities and properties defined by another template type (parent class)",
    "Polymorphism": "The concept that permits actions (methods) to share the same name but operate differently based on the context of the object involved",
    "Encapsulation": "The practice of gathering related data and methods inside a template, controlling access to its various internal parts",
    "Keywords": "Predefined and reserved words that possess special meanings and are used to establish the syntax and rules of the language",
    "Identifier": "A user-defined name given to a variable, reusable code block, or template to make the program understandable",
    "Tuple": "An *ordered collection* of objects that is defined by comma separation and is restricted from being modified after its initial creation"
}
wordIndex = [
    "Boolean",
    "if else Statement",
    "elif Statement",
    "Nested if statement",
    "for Loop",
    "while Loop",
    "break Statement",
    "continue Statement",
    "Python Functions",
    "def keyword",
    "Class",
    "Object",
    "__init__() Function",
    "Self Parameter",
    "Inheritance",
    "Polymorphism",
    "Encapsulation",
    "Keywords",
    "Identifier",
    "Tuple"]

#Assign a random word
random = random.randint(0, 19)
selectedWord = wordIndex[random]
lowercase = selectedWord.lower()
finalWord = selectedWord.replace(" ","|")
attempts = 0

#Word encryption
blanks = [0] * len(selectedWord)
Theword =  [0] * len(selectedWord)
for i in range(len(selectedWord)):
    Theword[i] = finalWord[i]
    if selectedWord[i] != " ":
        blanks[i] = "_"
    else:
        blanks[i] = "|"

#guess
print("Guess the word in 6 attempts. Type clue for the definition if you want clues.")
print(*blanks, sep=" ")
guess(input("Enter a letter: "))
