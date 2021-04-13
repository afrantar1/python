import random

secret = random.randint(1, 30)
attempts = 0
attempts_int = 0


while True:
    attempts_int +=1
    print(f"This is attempt number {attempts_int}")
    guess = int(input("Guess the secret number (between 1 and 30): "))


    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        #save number of attempts to score file
        with open("secret_score.txt", "r") as secret_score_file:
            score_in_file = int(secret_score_file.read())
        is_score_better = attempts_int < score_in_file

        # če je boljše število poskusov kot je zapisano v txt  datoteki, zapisi to število
        if is_score_better:
            print("Your score is the best score")
        # write num of attempts
        with open("secret_score.txt", "w+") as secret_score_file:
            secret_score_file.write(str(attempts_int))

        if not is_score_better:
            print("Your score is not the best score")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")