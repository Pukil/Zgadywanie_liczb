from random import randint


def new_game():
    computer_number = randint(1, 100)
    guess = lucky_guess()
    while guess != computer_number:
        if guess < computer_number:
            print("Too small!")
        else:
            print("Too big!")
        guess = lucky_guess()
    print("You win!")


def lucky_guess():
    while True:
        try:
            user_guess = int(input("Guess the number: \n"))
            return user_guess
        except ValueError:
            print("It's not a number!\n")


new_game()
