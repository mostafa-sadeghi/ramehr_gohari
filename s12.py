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
    numGuesses = 1
    # گرفتن حدس کاربر
    # بررسی وضعیت حدس کاربر(تابع)
        # یک تابع بنویس
        # این تابع مسئول بررسی حدس کاربر می باشد
        # اگر حدس کاربر درست بود : return 'you won'
        # اگر تمام ارقام غلط بودند return 'bagels'
        # اگر بعضی ارقام درست بودند بازیکن را راهنمایی نماید
            # با کمک حلقه فور تک تک ارقام عدد حدس زده شده را با عدد اصلی مقایسه نماید
            # یک لیست بساز
            # در صورتی که هر یک از ارقام درست بودند و سر جای خود بودند برای هریک عبارت زیر را در لیست اضافه کن
            # fermi
            # اگر هر یک از ارقام درست بودند اما در جای اشتباه بودند، 
            # pico را اضافه کن
        # در انتهای هر دست از بازیکن سوال شود که آیا می خواهی ادامه بدهی؟
        # در صورت مثبت ودن پاسخ، بازی ادامه یابد
        # در غیر اینصورت بازی تمام شود.
