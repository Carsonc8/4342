import re
import sys
"""
    Types of Tokens:
    Special
    Identifier
    Data Type
    Reserved
    Assignment
    Multiplication
    Relation
    Reserved
    Addition
    Integer
"""

RESERVED_TOKENS = {}
# r converts it to a raw string. Then reads as any letter from a-zA-Z along with an _
IDENTIFIER_REGEX = [r'[a-zA-Z_d]\w*']
INTEGER_TOKENS = ''
SPECIAL_TOKENS = ''

for patterns in IDENTIFIER_REGEX:
    wow = re.findall(patterns, "f")
print(wow)
if wow:
    print("Valid Identifier")
else:
    print("Not Valid Identifier")