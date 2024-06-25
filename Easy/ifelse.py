#!/usr/bin/env python3

"""
Given an integer, , perform the following conditional actions:
    1) If  is odd, print Weird
    2) If  is even and in the inclusive range of  to , print Not Weird
    3) If  is even and in the inclusive range of  to , print Weird
    4) If  is even and greater than , print Not Weird
"""


import math
import os
import random
import re
import sys


def main():
    """
    Main function
    """
    n = int(input().strip())

    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 5):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


if __name__ == "__main__":
    main()
