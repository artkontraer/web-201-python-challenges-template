# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

from operator import neg


def extract_integers(mixed_list):
    if not isinstance(mixed_list, list):
       return "This is not a list"


    list_only_int = []  
    for i in mixed_list: 
        if isinstance(i,int):
            list_only_int.append(i)
    return list_only_int

def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]   

def test_challenge_05_happy_case_2(): 
     assert extract_integers(['apple', 'banana', 'plum']) == [] 

def test_challenge_05_happy_case_3(): 
     assert extract_integers([1.5, 2.3]) == []   

def test_challenge_05_happy_case_4(): 
     assert extract_integers('apple') == "This is not a list"

def test_challenge_05_sad_case(): 
     assert extract_integers(123) == "This is not a list"  