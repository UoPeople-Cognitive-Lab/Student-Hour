# POW
# is_power(x ,y ) keeps returning None instead of True or False. Pleas help.
# Fixed!


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


# Return True if x is an integer power of y, otherwise False
# Expects both arguments to be nonzero

def is_power(x,	y):
    if x == y:  # base case where x/y == 1
        return True
    elif y == 1:  # base case where y == 1 but x does not
        return False
    else:
        return is_divisible(x, y) and is_power(x/y, y)

# def is_power(x, y):
#     if x == y:                  # Check for equal terms
#         return ' x = y'
#     elif y == 1:                # Check for second term equal to one
#         return ' y = 1 '
#     if is_divisible(x, y) == True:
#         # is_power(x, y) Problem:Keep getting None returned
#         x = x / y
#        is_power(x, y)          # Function Calls itself has value of None?
#     else:                       # I tried if then loop keep getting same return of None
#         print(' returning value is: ', x == 1)
#         return     # x == 1    # Return True or False State


def main():
    # Keep Getting None returned instead of False
    print("is_power(10, 2) returns: ", is_power(10, 2))
    # Keep Getting None returned instead of True
    print("is_power(27, 3) returns: ", is_power(27, 3))
    print("is_power(1, 1) returns: ", is_power(1, 1))
    print("is_power(10, 1) returns: ", is_power(10, 1))
    print("is_power(3, 3) returns: ", is_power(3, 3))


main()
