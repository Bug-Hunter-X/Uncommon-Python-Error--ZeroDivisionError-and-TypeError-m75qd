# Uncommon Python Error: ZeroDivisionError and TypeError
This repository demonstrates an uncommon error in Python that often goes unnoticed: a `ZeroDivisionError` and a `TypeError` when using 0 as the denominator in a division and when inputs are not numbers. The code example shows the error, while the solution implements robust error handling.

## Error Description
The `ZeroDivisionError` occurs when dividing by zero, which is mathematically undefined. The `TypeError` happens when trying to perform arithmetic operation on incompatible data types, such as dividing a number by a string.

## Solution
The solution includes a try-except block to catch the `ZeroDivisionError` and handles the case where the denominator is zero. It also includes type checking to prevent `TypeError`.