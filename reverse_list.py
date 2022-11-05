# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/05/2022
# Description: Write a function named reverse_list that takes as a parameter
# a list and reverses the order of the elements in that list.

def reverse_list(vals):
    """ Takes a list of integers and reverses the order of the original list. """
    ind = 0
    int = len(vals) - 1

    while ind < int:
        """ While loop reverses the order of the list. """
        obj = vals[ind]
        vals[ind] = vals[int]
        vals[int] = obj
        ind = ind + 1
        int = int - 1


# vals = [7, -3, 12, 9]
# reverse_list(vals)

# print(vals)
