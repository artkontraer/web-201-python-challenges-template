# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.


def sum_of_squares(array_of_numbers):
    if not isinstance(array_of_numbers, list):
        return "Not a list"

    sum = 0
    for i in array_of_numbers:
        if isinstance(i, int):
            sum = (i * i) + sum
        if not isinstance(i, int):
            return("No integer")
    return (sum)

        
         
def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30

def test_challenge_06_happy_case_2(): 
     assert sum_of_squares([7,1, 50]) == 2550

def test_challenge_06_happy_case_3(): 
     assert sum_of_squares(["a", "b", "c", "d"]) == "No integer"

def test_challenge_06_happy_case_4(): 
     assert sum_of_squares(["aloha"]) == "No integer"

def test_challenge_06_sad_case(): 
     assert sum_of_squares() == "Not a list"      
# QUESTION: why cant brackets be empty? what condition would have to be pronounced to return "Not a list" in case 
# there is no valid entry?

