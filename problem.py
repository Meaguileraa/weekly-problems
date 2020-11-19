
#This file has the weekly wednesday HB problems

#11/18 

####################################################################

#1. Max Number 

def max_num(num_list):
    """Returns largest integer from given list"""

    return max(num_list)

print(max_num([5, 3, 6, 2, 1])) #6



#2. Count List Recursively 

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if lst == []:
        return 0
    
    return 1 + count_recursively(lst[1:])

print(count_recursively([])) #0
print(count_recursively([1, 2, 3])) #3



#3. Reverse Linked List 


####################################################################