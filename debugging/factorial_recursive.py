#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Compute the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial of n (n!).
             By definition, 0! = 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    # Take the first command-line argument, convert to int, and print factorial
    f = factorial(int(sys.argv[1]))
    print(f)
