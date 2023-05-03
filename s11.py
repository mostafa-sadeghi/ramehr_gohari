# message = "you and me and sara are friends."
# print(message.find("and"))
# print(message.count("and"))
# print(message.split().count("and"))


# string = ''
# all_words = []
# index = 0
# for char in message:
#     index += 1
#     string += char
#     if char == ' ' or index == len(message):
#         all_words.append(string[:-1])
#         string = ''

# print(all_words)

# counter = 0
# for word in all_words:
#     if word == 'and':
#         counter += 1

# print(f'"and" repeated "{counter}" times in "{message}"')


import random


# print(random.random()) # [0,1)
# print(random.randint(100,999))
# print(random.randrange(100,1000,50))
# print(random.choice(["red","green","blue"]))
# print(random.choice([1,2,3,45]))
# print(random.choice('abc'))
# print(random.choices([1,2,3,4,5,6,7,8,9],k=3))


def find_digits(number):
    digits = {}
    is_unique = True
    i = 1
    while number != 0:
        digits[f'{i}'] = number % 10
        number = number // 10
        i += 1
    for i in range(len(digits.values())):
            if list(digits.values())[i] in list(digits.values())[i+1:]:
                 is_unique = False
    if is_unique == False:
        return find_digits(random.randrange(100,1000))
                 
   
    return digits.values()

number = random.randrange(100,1000)
print(find_digits(number))











# import random

# NUMBER_DIGITS = 3
# MAXIMUM_TIMES = 10
# print(f'''
# I am thinking of a {NUMBER_DIGITS}-digit number. Try to guess what it is.
# The clues I give are...
# When I say:    That means:
#   Bagels       None of the digits is correct.
#   Pico         One digit is correct but in the wrong position.
#   Fermi        One digit is correct and in the right position.
# I have thought up a number. You have {MAXIMUM_TIMES} guesses to get it.
# ''')

# secret_number = generate_secret_number()