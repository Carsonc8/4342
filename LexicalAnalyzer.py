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
ADDITION_TOKEN = [r'+',r'-',r'or',]
MULTIPLYING_TOKEN = [r'*',r'div',r'and',]
SPECIAL_KEYWORD = [r'',]
ASSIGNMENT_OPERATOR = [r':=',]
RELATIONAL_TOKEN = [r'=',r'<>',r'<',r'<=',r'>='r'>']
DATA_TYPE_TOKEN = [r'Integer',r'Boolean',r'true',r'false']





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


def readFile():
    with open("input.txt", "r") as f:
        for line in f:
            for word in line.split():
                if word == "program":
                    print("yes")
            else:
                print("Asdfasdf")
def main():
    readFile()

if __name__ == "__main__":
    main()