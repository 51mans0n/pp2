import random
def guessGame():
    guessNum = random.randint(1, 20)
    count = 0
    number = 0
    name = input("Hello! What is your name?\n")
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    while(number != guessNum):
        number = int(input("Take a guess\n"))
        count += 1
        
        if(number < guessNum):
            print("\nYour guess is too low.")
            
        elif(number > guessNum):
            print("\nYour guess is too big.")
            
    print(f"Good job, {name}! You guessed my number in {count} guesses!")
guessGame()