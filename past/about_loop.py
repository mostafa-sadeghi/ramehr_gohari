

# for i in range(5):
#     print("ok", end=" ")
#     print("in")
# print("out")


# use for loop to take 4 names from input and then append them to list
# print all names from the list with for loop
# names = []
# for i in range(4):
#     n = input('enter a name: ')
#     names.append(n)

# print("all names as list :", names)
# print("length of list :", len(names))
# for i in range(len(names)):
#     print(names[i])

import time
for i in range(10):
    print(i)
    time.sleep(1)

for i in range(1, 10):
    print(i)
    time.sleep(1)
for i in range(2, 12, 2):  # range parameters are : start point & end point & step
    print(i)
    time.sleep(1)

# exercise 1 : write a program that calculates sum of even number from 1,000,000 to 10,000,000
# exercise 2 : do above for odd numbers
for i in range(5):
    print((i+2)*5)

for i in range(10, -1, -1):
    print(i)
