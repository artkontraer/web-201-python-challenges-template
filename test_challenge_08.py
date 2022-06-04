# Problem 1:
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three, print Fizz instead of the number, 
# and multiples of five, print Buzz. 
# For numbers that are multiples of both three and five, print FizzBuzz

# sample output:
# 1, 2, Fizz, 4, Buzz, 5, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz ... and so on ..

def print_fizz_in_hundred(one_hundred):
    one_hundred = range(1, 101)
    
    for i in one_hundred:
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        if i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(str(i))

print_fizz_in_hundred([15])


# def test_challenge_08_happy_case(): 
#      assert print_fizz_in_hundred([15]) == (["FizzBuzz"])