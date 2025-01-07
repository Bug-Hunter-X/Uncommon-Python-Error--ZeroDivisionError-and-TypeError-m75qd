def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return a / b
            else:
                raise TypeError("Inputs must be numbers.")
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

# Example usage:
result1 = function_with_uncommon_error(5, 0)  # Output: Division by zero
result2 = function_with_uncommon_error(0, 5)  # Output: 5
result3 = function_with_uncommon_error(5, 2)  # Output: 2.5
result4 = function_with_uncommon_error("5", 2) # Output: Inputs must be numbers.
print(result1)
print(result2)
print(result3)
print(result4)