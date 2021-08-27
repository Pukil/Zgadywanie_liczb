from random import randint


def new_game():
    """
    Game function
    :return: None
    """
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
    """
    Gets guess number from user.
    While loop with try/except allows to retry entering the number if entered wrong type, for example string.
    :return: user's guess as an int
    """
    while True:
        try:
            user_guess = int(input("Guess the number: \n"))
            return user_guess
        except ValueError:
            print("It's not a number!\n")


new_game()
