# Create a Python function that accepts a string. 
# The function should return a string, with each 
# character in the original string doubled. 
# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", 
# it should return "112233aa!!".

def duplicate_characters(str):
     for character in str: 
          character = 2 * character
          return(character)
     print(character)

     double = [] 
     for i in str:
          double.append(i+""+i)
     # print("".join(double))

     print("".join(double))
     # return double

# duplicate_characters("super")

     
def test_challenge_02_case_1(): 
     assert duplicate_characters('now') == 'nnooww'

def test_challenge_02_case_2(): 
     assert duplicate_characters('123a!') == '112233aa!!'