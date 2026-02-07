#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Recursively computes the factorial of a non-negative integer.

    Parameters:
        n (int): The number to compute the factorial for.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
