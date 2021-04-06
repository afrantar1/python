secret = 22
guess = 0

did_guess_secret = False

while not did_guess_secret: #True
    #Do all this
    guess = int(input("Guess the secret number (between 1 and 30): "))
    did_not_guess_secret = guess == secret
    if guess == secret:
        print("You guessed it - congratulations! It's number 22.")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

print("End")

