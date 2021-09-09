import random

x = 0

def startGame():
  global x
  x = random.randint(0, 100)

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
