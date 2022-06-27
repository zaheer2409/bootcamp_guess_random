"""Guess the number between 1 and 100 randomly chosen by the computer.
    You will be prompted whether your guess is lower or higher than the number. """
import random


def generate_random() -> int:
    """This method generates a random integer value between 1 and 100
        ReturnValue:
            random_number: A random integer between 1 and 100"""
    random_number = random.randint(1, 100)
    return random_number


def enter_your_guess() -> int:
    """This method accepts a number between 1 and 100 as user input and validates its value
        ReturnValue:
            int(guess): This is the VALID value of the guess made by the user"""
    while True:
        try:
            guess = input("Enter your guess. Make sure it is an integer number between 1 and 100!\n")
            assert guess.isdigit(), "Error! Make sure your guess is a valid integer number between 1 and 100"
            guess = int(guess)
            assert 1 <= guess <= 100, "Error! Make sure your guess is an integer between 1 and 100"
            return guess
        except AssertionError as e:
            print(e)


def compare_numbers(number:int, guess:int)-> int:
    """This method returns -1, 0 or 1 if the guessed number is lower, equal to or higher than the random number.
        Parameters:
            number: A random number between 1 and 100
            guess: A number between 1 and 100, guessed by the user
        ReturnValue:
            outcome: -1, 0 or 1 depending on the comparison of the two numbers"""
    if guess < number:
        outcome = -1
    elif guess == number:
        outcome = 0
    elif guess > number:
        outcome = 1
    return outcome


def determine_message(outcome:int)->str:
    """This method returns the appropriate message depending on the outcome (-1,0,1)
        Parameters:
            outcome: A number from the list of [-1,0,1]
        ReturnValue:
            msg: A message computed depending on the outcome"""
    list_of_messages = [print_lower(),print_equal(),print_higher()]
    msg = ""
    if outcome == -1:
        msg = list_of_messages[0]
    elif outcome == 0:
        msg = list_of_messages[1]
    elif outcome == 1:
        msg = list_of_messages[2]
    return msg


def print_equal() -> str:
    """Returns an appropriate message if the guessed value is equal to the random number
        ReturnValue:
            response: Appropriate message"""
    response = "YOU GUESSED THE CORRECT NUMBER! WELL DONE!."
    return response


def print_higher() -> str:
    """Returns an appropriate message if the guessed value is higher than the random number
        ReturnValue:
            response: Appropriate message"""
    response = "You guessed higher! Try again."
    return response


def print_lower() -> str:
    """Returns an appropriate message if the guessed value is less than the random number
       ReturnValue:
            response: Appropriate message"""
    response = "You guessed lower! Try again."
    return response


if __name__ == "__main__":
    random_number = generate_random()
    guessed = False
    while not guessed:
        user_guess = enter_your_guess()
        outcome = compare_numbers(random_number,user_guess)
        if outcome == 0:
            print(determine_message(outcome))
            guessed = True
        else:
            print(determine_message(outcome))


