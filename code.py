import random

minr=0
maxr=10

num=0

def isInt(number):
    if number != int(number):
        print("Error: Guess could not be converted to a type 'int'")
    else:
        return number

def checkIfIsInRange(guess):
   if num > maxr:
        print ("Error: Guess to large. Must be in the range ("+minr+"-"+maxr+")")
        return False
   else:
        return True
   if num < minr:
        print ("Error: Guess to small. Must be in the range ("+minr+"-"+maxr+")")
        return False
   else:
        return True

def getRadomINT():
    rand_intt = random.randint(minr, maxr)
    return rand_intt
def guessSelector():
    rand_int = getRadomINT()
    guess_no_int = input("Guess: \n")
    print(rand_int)
    guess=int(guess_no_int)
    isInt(guess)
    checkIfIsInRange(guess)
    if guess == rand_int:
        print("Correct! ")
    else:
        if guess < rand_int:
            print("Guess to small")
            guessSelector()
        if guess > rand_int:
            print("Guess to large")
            guessSelector()
        
guessSelector()
        
