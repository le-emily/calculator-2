"""Math functions for calculator."""


def add(num1):
    """Return the sum of the two input integers."""
    total = reduce(lambda x, y: x + int(y), num1)
    return total


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    for num in num2:
        num1 = num1 - int(num)
    return num1


def multiply(num1, num2):
    """Multiply the two inputs together."""
    for num in num2:
        num1 = num1 * int(num)
    return num1


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""
    num1 = float(num1)
    for num in num2:
        num1 = num1 / int(num)
    return num1


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
