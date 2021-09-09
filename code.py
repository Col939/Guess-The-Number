import random

x = 0

def startGame():
  x = random.randint(0, 100)
  print(x)
startGame()  

def checkGuess():
    
    guess = input("What is the Number?")
    intGuess = int(guess)
    
    if intGuess == x:
        
        print("You Win!")
    else:
        print(intGuess == x)
        print("Try Again :(")
        checkGuess()
        
checkGuess()
