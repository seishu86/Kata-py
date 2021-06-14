
# Given a month as an integer from 1 to 12, 
# return to which quarter of the year it belongs as an integer number.

def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4