# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")


# total = 0
# for i in range(3):
#     new_number = int(input('enter a number:> '))
#     total += new_number

# print("the total is:", total)


# total = 0
# for i in range(1,101):
#     total += i
# print(total)


# total = 0
# for i in range(5):
#     new_number = int(input('Enter a number:> '))
#     if new_number == 0:
#         total += 1
# print("you entered a total of", total, "zeros")

# numbers = [1, 2, 3, 4, 5, 2, 3, 0]
# number_to_find = 2

# counter = 0
# for n in numbers:
#     if n == number_to_find:
#         counter += 1
# print(f'{number_to_find} repeated {counter} time/s.')

# print(f'{number_to_find} repeated {numbers.count(number_to_find)} time/s.')

# تمرین اول
'''
برنامه ای بنویسی که 5 عدد از ورودی دریافت نماید
و مجموع اعداد فرد وارد شده و نیز مجموع اعداد زوج وارد شده را نمایش دهد
همچنین اعداد را از انتها به ابتدا نمایش دهد

'''

# a = 0
# for i in range(10):
#     a = a + 1
# print(a)

# for j in range(10):
#     a = a + 1
# print(a)


# a = 0
# for i in range(10):
#     a = a + 1
#     for j in range(10):
#         a = a + 1

# print(a)


# while loop

for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i = i + 1  # i += 1
