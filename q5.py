def check_divisibility(num, divisor):

    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both num and divisor must be numeric.")

    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")

    return num % divisor == 0

# Task 2:
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
