"""Math functions for calculator."""


def add(num):
    """Return the sum of the two input integers."""
    return reduce(lambda x, y: int(x) + int(y), num) 

def subtract(num):
    """Return the second number subtracted from the first."""
    return reduce(lambda x, y: int(x) - int(y), num)


def multiply(num2):
    """Multiply the two inputs together."""
    return reduce(lambda x, y: int(x) * int(y), num)


def divide(num):
    """Divide the first input by the second, returning a floating point."""
    return reduce(lambda x, y: int(x)/int(y), num)


def square(num):
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
