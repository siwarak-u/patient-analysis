"""
This module counts the number of line in standard input
Input: a string
"""


import sys

count = 0

for line in sys.stdin:

	count += 1

print (count, "line in standard input")


