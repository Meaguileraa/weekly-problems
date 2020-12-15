
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

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        Node(3).as_string()
        '3'

        Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)
    
    def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    ll = Node(1, Node(2, Node(3)))
    reverse_linked_list(ll).as_string()
    '321'
    """

ll = Node(1, Node(2, Node(3)))
new_ll = reverse_linked_list(ll)
new_ll.as_string() #'321'

####################################################################

#12/15 

#1. Balanced Parenthesis


# Given a string, return True or False depending on whether that string has balanced parentheses.

# For the purposes of this problem, you only need to worry about 
# parentheses (( and )), not other opening-and-closing marks, like curly brackets, 
# square brackets, or angle brackets.


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""





print(has_balanced_parens("()")) #True
print(has_balanced_parens("(Oh Noes!)(")) #False
print(has_balanced_parens("((There's a bonus open paren here.)")) #False
print(has_balanced_parens(")")) #False
print(has_balanced_parens("(")) #False
print(has_balanced_parens("(This has (too many closes.) ) )")) #False









#2. Is Palidrome
#3. Spiral 
