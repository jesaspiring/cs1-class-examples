import random

numGuess = 0
guessLimit = 5
randomNum = random.randint(0, 100)
userInput = int(input("Enter your guess: ")) # string -> integer
haveGuessed = True

while userInput != randomNum:

    guessLimit-=1
    if(guessLimit > 0):
        
        if(userInput > randomNum):
            print("+------+")
            print("Lower")
            print("+------+")
        elif(userInput < randomNum):
            print("+------+")
            print("Higher")
            print("+------+")

        numGuess+=1
        print("Remaining guess: ", guessLimit)
        userInput = int(input("Guess again: "))
        
    else:
        print("+=============================+")
        print("Sorry, try some other time")
        print("Remaining guess: ", guessLimit)
        print("The random number is: ", randomNum)
        print("+=============================+")
        haveGuessed = False
        break
        

if(haveGuessed):
    print("+==============================================+")
    print("Congratulations! You have guessed the number")
    print("The random number: ", randomNum)
    print("Number of tries: ", numGuess) 
    print("+==============================================+")

