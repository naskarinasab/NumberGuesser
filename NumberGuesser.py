from random import *

wrongInput = True #General variable for any wrong inputs

#GETTING RANGE FOR RANDOM NUMBER
while(wrongInput):
    startingLimit = int(input("What is the starting number of your range? "))
    endingLimit = int(input("What is the ending number of your range? "))
    if(startingLimit >= endingLimit):
        print("Your starting limit is bigger than your ending limit. Try again.")
        continue
    wrongInput = False


#GENERATING RANDOM NUMBER
num = randint(startingLimit, endingLimit)
wrongInput = True #Resetting the check variable
print("Okay, the random number has been generated.")

#GAME PORTION
while(wrongInput):
    guess = 0
    #Getting input but also making sure the input is valid
    while(guess == 0):
        guess = int(input("What do you think the number is? Pick between {:d} and {:d} ".format(startingLimit, endingLimit)))
        if((guess<startingLimit) or (guess>endingLimit)):
            print("That is not a valid choice, try again")
            guess = 0
    #Comparing guesses and giving hints if incorrect
    if(guess == num):
        wrongInput = False
    elif(guess > num):
        print("Your guess is LARGER than the actual number. Try again.")
    elif(guess < num):
        print("Your guess is LESS than the actual number. Try again")


print("You guessed correctly! Well done!")
