#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
#n is odd
    if n % 2 == 1:
        print("Weird")
#n is even AND within inclusive range of 2 to 5
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
#n is even AND within inclusive range of 6 to 20
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
#n greater than 20
    else:
        print("Not Weird")
