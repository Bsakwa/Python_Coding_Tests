#!/usr/bin/python3

"""
This code takes numbers from the STDIN and 
  1) prints the sum of the numbers on the first line
  2) prints the difference of the numbers on the second line
  3) prints the product of the numbers on the third line
"""

import sys

def main():
    """
    Declare two integers a and b
    """
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())

    print(a + b)
    print(a - b)
    print(a * b)

if __name__ == "__main__":
    main()
