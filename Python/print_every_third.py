# Author: Jeffrey Romero
# Date: 2/10/2021
# 
# Prints every third element of a list using recursion.

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_list_recursive(index):
    if index < len(myList):
        if (index + 1) % 3 == 0: # myList is 0-indexed so add 1 to index
            print(myList[index])
        print_list_recursive(index + 1)


print_list_recursive(1) # 1-indexing
