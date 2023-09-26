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


# r converts it to a raw string. Then reads as any letter from a-zA-Z along with an _ that allows any combination of letters.
IDENTIFIER_REGEX = [r'[a-zA-Z_d]\w*']
#any numbers with any combination
INTEGER_TOKENS = ['\d+']
ADDITION_TOKEN = []
MULTIPLYING_TOKEN = []
SPECIAL_KEYWORD = []
ASSIGNMENT_OPERATOR = []
RELATIONAL_TOKEN = []
DATA_TYPE_TOKEN = []

"""
for patterns in IDENTIFIER_REGEX:
    alpha = re.findall(patterns, "f")

if alpha:
    print("Valid Letter Identifier")
else:
    print("Not Valid Identifier")
for numPatterns in INTEGER_TOKENS:
    num = re.findall(numPatterns, "30")
if num:
    print("Valid Number Identifier")
else:
    print("Not Valid Identifier")
for specialPat in SPECIAL_TOKENS:
    special = re.findall(specialPat, ";")
if special:
    print("Valid Special Identifier")
else:
    print("Not Valid Identifier")
"""
