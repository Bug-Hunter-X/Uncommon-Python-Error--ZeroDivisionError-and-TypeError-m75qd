def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct return statement
    elif b == 0:
        return a  # Correct return statement
    else:
        return a / b

# This will cause a ZeroDivisionError if the denominator is 0:
result = function_with_uncommon_error(5, 0)
print(result)
# This will cause a TypeError if a is not a number and b is 0: