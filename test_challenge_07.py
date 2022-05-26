# Supermarket billing: Write a function in python that 
# takes a shopping list (dictionary of items and price) and returns the total.
# extension: apply discount accordingly:
# if total is greater than 50 Euros 5% discount.
# if total is greater than 60 Euros 6% discount.
# if total is greater than 70 Euros 7% discount and so on.

def calculate_bill(shopping_list):
    sumItems = sum(shopping_list.values())
    discount = (sumItems // 10) * sumItems / 100
    if sumItems > 50:
        sumItems -= discount
    return(sumItems)
    # else:
    #     return(sumItems)

# shopping_list = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}


def test_challenge_07_happy_case(): 
    shopping_list = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == 43.4

def test_challenge_07_happy_case_2(): 
    shopping_list = {'apples':15, 'bananas':20, 'eggs':16}
    assert calculate_bill(shopping_list) == 48.45