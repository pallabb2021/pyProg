import random


def guessing_game():
    """
    This function takes no argument, the user is prompted to enter a number which will be compared to guessed number and
    appropriate response will be sent to user!
    :return:
    """
    random_number = random.randrange(0, 101)
    print(random_number)
    GUESS_LIMIT=0
    print("Would you like a guess limit (enter a positive number) otherwise you cannot quit unless you win the game!")
    try:
        user_guess_limit = int(input("Enter your option here : "))
    except ValueError:
        user_guess_limit = 'NO_USER_INPUT'
    if isinstance(user_guess_limit,int):
        GUESS_LIMIT = user_guess_limit
    else:
        NO_USER_INPUT=True
        pass
    while True:
        if GUESS_LIMIT > 0:
            GUESS_LIMIT-=1
        user_input = int(input("Enter the guessed number: "))
        if user_input == random_number:
            print(f"You guessed it right!, number is indeed {user_input}")
            break
        elif user_input >= random_number:
            print(f"Guessed number is too high!")

        elif user_input <= random_number:
            print(f"Guessed number is too low!")

        if GUESS_LIMIT ==0 and NO_USER_INPUT != True:
            print('You exceeded the guesses, quitting the game!')
            break

if __name__ == '__main__':
    print("Calling main!")
    guessing_game()
