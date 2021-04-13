import random
secret = random.randint(1,30)
guess = None

did_guess_secret = False

while  not did_guess_secret: #True

    guess = int(input("Guess the secret number (between 1 and 30): "))
    id_not_guess_secret = guess == secret
    did_guess_secret = guess == secret
    if did_guess_secret:
        print("You guessed it - congratulations! It's number 22." + str(secret))
        break



