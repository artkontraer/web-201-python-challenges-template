# It takes 21 seconds to wash your hands 
# and help prevent the spread of COVID-19.
#
# Create a function that takes the number of times 
# a person washes their hands per day (n) 
# and the number of months (m) they follow this routine, 
# and calculates the duration in minutes and seconds 
# that person spends washing their hands.
#
# Examples:
# wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
# wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
# wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
# 
# Notes: Consider a month has 30 days.

def wash_hands(n, m):
    # n = number of washes
    # m = number of months
    oneTime = 21
    oneDayTotalSeconds = oneTime * n
    totalWashes = oneDayTotalSeconds * 30 * m
    minutes = int(totalWashes // 60) 
    seconds = int(totalWashes % 60)

    return(str(minutes) + " minutes and " + str(seconds) + " seconds")


def test_challenge_03_case_1(): 
    assert wash_hands(8, 7) == '588 minutes and 0 seconds'

def test_challenge_03_case_2():
    assert wash_hands(1.5, 3) == "47 minutes and 15 seconds"

def test_challenge_03_case_3():
    assert wash_hands(0, 0) == "0 minutes and 0 seconds"