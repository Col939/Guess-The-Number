import random

x = 0

def startGame():
  global x
  x = random.randint(0, 100)
  print(x)
startGame()  

def checkGuess():
    print("What is the Number?")
    guess = input("")
    intGuess = int(guess)
    
    if intGuess == x:
        
        print("You Win!")
    else:
        print("Try Again :(")
        checkGuess()
        
checkGuess()
