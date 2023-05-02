# shopping_list = ['item1', 'item2', 'item3', 1, True, False]
# print(shopping_list[0])
# print(shopping_list[1])

# last item:

# print(shopping_list[-1])

# slice_1 = shopping_list[1:3]
# print("slice 1 :", slice_1)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_numbers = numbers[::2]
# print("odd_numbers:", odd_numbers)

# exercise 2 : print even numbers from above list
# exercise 3 : calculate the sum of all numbers in above list


shopping_list = []
print("shopping list before adding something:", shopping_list)

shopping_list.append("egg")
shopping_list.append("banana")
shopping_list.append("pen")
shopping_list.append("tomato")
shopping_list.append("milk")

print("shopping list after adding items:", shopping_list)

print("enter a new item to add in the list:")
new_item = input('> ')

shopping_list.append(new_item)
print("shopping list after adding new item:", shopping_list)

del shopping_list[0]
print("shopping list after removing first item:", shopping_list)

print("enter product name to remove from list")
remove_item = input('> ')
shopping_list.remove(remove_item)
print("shopping list after removing entered item:", shopping_list)
