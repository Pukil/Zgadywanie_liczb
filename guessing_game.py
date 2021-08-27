from random import randint

computer_guess = randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number: \n"))
        if guess < computer_guess:
            print("Too small!\n")
        elif guess > computer_guess:
            print("Too big!\n")
        else:
            print("You win!")
            break
    except ValueError:
        print("It's not a number!\n")
