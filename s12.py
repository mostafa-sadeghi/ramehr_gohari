import string
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_secret_number():
    """This function creates 3 digits random number with non repeating digits"""
    numbers = list(string.digits)
    random.shuffle(numbers)
    secret_number = ''.join(numbers[:3])
    return secret_number


def check_state(user_guess, sec_number):
    print("user_guess", user_guess)
    print("sec_number", sec_number)
    # todo 
    


print(f'''I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.
The clues I give are...
When I say:    That means:
  Bagels       None of the digits is correct.
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
I have thought up a number. You have {MAX_GUESSES} guesses to get it.
''')

while True:
    secret_number = generate_secret_number()
    print('Secret number is generated...')

    for i in range(10):
        print(f'you have {MAX_GUESSES-i} times to guess it!')
        guess = input('Enter three digits number: ')
        state = check_state(guess, secret_number)
