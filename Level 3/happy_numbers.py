"""
Write a method to determine whether a postive number is Happy.

A number is Happy (Yes, it is a thing!) if it follows a sequence that ends in 1 after following the steps given below : 

Beginning with the number itself, replace it by the sum of the squares of its digits until either the number becomes 1 or loops endlessly in a cycle that does not include 1. 
For instance, 19 is a happy number. 
   Sequence:

      12 + 92 = 82

      82 + 22 = 68

      62 + 82 = 100

      12 + 02 + 02 = 1


Example:
Input : 19 
Output: true 
"""

def is_happy_number(number):
    if number == 1:
        return True
    elif len(str(number)) == 1 and number != 1:
        return False
    else:
        sum = 0
        number = str(number)
        for i in number:
            sum += int(i)**2
        return is_happy_number(sum)