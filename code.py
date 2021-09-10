import random

x = 0

def startGame():
  global x
  x = random.randint(0, 100)
startGame()  

def checkGuess():
    print("What is the Number?")
    guess = input("")
    intGuess = int(guess)
    
    if intGuess == x:
        
        print("You Win!")
    elif intGuess > x:
      
      print("Too High!")
      checkGuess()
            
    elif intGuess < x:
      
      print("Too Low!") 
      checkGuess()
        
checkGuess()
