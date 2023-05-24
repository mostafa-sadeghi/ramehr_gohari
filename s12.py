import string
import random
from colorama import Fore, Back, Style


NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_secret_number():
    """This function creates 3 digits random number with non repeating digits"""
    numbers = list(string.digits)  # ['0','1',....]
    random.shuffle(numbers)
    secret_number = ''
    for n in numbers:
        secret_number += n
    return secret_number[:3]


def check_state(user_guess, sec_number):
    if user_guess == sec_number:
        return 'You Won!!'
    # user_guess = '678'      sec_number = '351'     =>    ['pico', 'pico']
    help_list = []
    for i in range(len(user_guess)):
        if user_guess[i] == sec_number[i]:
            help_list.append('Fermi')
        elif user_guess[i] in sec_number:
            help_list.append('Pico')
    if len(help_list) == 0:
        return 'Bagels'
    return help_list


while True:
    print(f'''I am thinking of a {Style.RESET_ALL}{Fore.RED+Back.GREEN}{NUM_DIGITS}-digit number{Style.RESET_ALL}. Try to guess what it is.
    The clues I give are...
    When I say:    That means:
    {Style.RESET_ALL}{Fore.RED+Back.CYAN}Bagels{Style.RESET_ALL}       None of the digits is correct.
    {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX+Back.RED}Pico{Style.RESET_ALL}         One digit is correct but in the wrong position.
    {Style.RESET_ALL}{Fore.LIGHTRED_EX+Back.YELLOW}Fermi{Style.RESET_ALL}        One digit is correct and in the right position.
    I have thought up a number. You have {MAX_GUESSES} guesses to get it.
    ''')

    secret_number = generate_secret_number()
    print('Secret number is generated...')

    for i in range(MAX_GUESSES):

        guess = input('Enter three digits number: ')
        state = check_state(guess, secret_number)
        print(state)
        if guess == secret_number:
            print("you won!!!")
            break
    user_input = input("Do you want to continue? (yes or no) ")
    if user_input == "no":
        break
