# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    count = 0
    for each_character in word:
        if each_character == 'a' or each_character == 'e' or each_character == 'i' or each_character == 'o' or each_character == 'u' or each_character == 'A' or each_character == 'E' or each_character == 'I' or each_character == 'O' or each_character == 'U':
            count = count + 1 
    return count

  
def test_challenge_01_happy_case(): 
     assert count_vowels('Kaleidoscope') == 6   
     assert count_vowels('Theresa') == 3

def test_challenge_01_emptycase():
    assert count_vowels ('') == 0
    assert count_vowels("brrr") == 0

def test_challenge_01_Upper_case():
    assert count_vowels('VOLUME') == 3
    #failed, therefore made changes to if-conditions and added UPPERCASE vowels

def test_challenge_01_mixed_types():
    assert count_vowels('Chanel No. 5') == 3
