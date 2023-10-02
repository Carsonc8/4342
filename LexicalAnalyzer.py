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
# any numbers with any combination
INTEGER_TOKENS = ['\d+']
ADDITION_TOKEN = [r'+',r'-',r'or',]
MULTIPLYING_TOKEN = ['*','div','and',]
SPECIAL_KEYWORD = ['begin','procedure',]
ASSIGNMENT_OPERATOR = [':=',]
RELATIONAL_TOKEN = ['=','<>','<','<=','>=''>']
DATA_TYPE_TOKEN = ['Integer','Boolean','true','false']





"""
for patterns in IDENTIFIER_REGEX:
    alpha = re.findall(patterns, "f")

IDENTIFIER_REGEX = [r'[a-zA-Z_d]\w*']
# any numbers with any combination
INTEGER_TOKENS = ['\d+']
ADDITION_TOKEN = [r'+',r'-',r'or',]
MULTIPLYING_TOKEN = [r'*',r'div',r'and',]
SPECIAL_KEYWORD = [r'',]
ASSIGNMENT_OPERATOR = [r':=',]
RELATIONAL_TOKEN = [r'=',r'<>',r'<',r'<=',r'>='r'>']
DATA_TYPE_TOKEN = [r'Integer',r'Boolean',r'true',r'false']

"""

def readFile():
    with open("input.txt".replace(r'\n', '\n'), "r") as f:
        readlines = f.readlines()

    for ir in IDENTIFIER_REGEX:
        for lines in readlines:
            if ir in lines:
                print(lines.strip()[0] + " : Identifier Token")
    for it in INTEGER_TOKENS:
        for lines in readlines:
            if it in lines:
                print(it + " : Integer Token")
    for adt in ADDITION_TOKEN:
        for lines in readlines:
            if adt in lines:
                print(adt + " : Addition Token")
    for multit in MULTIPLYING_TOKEN:
        for lines in readlines:
            if multit in lines:
                print(multit + " : Multiplying Token")
    for spect in SPECIAL_KEYWORD:
        for lines in readlines:
            if spect in lines:
                print(spect + " : Special Keyword Token")
    for asignt in ASSIGNMENT_OPERATOR:
        for lines in readlines:
            if asignt in lines:
                print(asignt + " : Assignment Token")
    for relt in RELATIONAL_TOKEN:
        for lines in readlines:
            if relt in lines:
                print(relt + " : Relational Token")
    for dtt in DATA_TYPE_TOKEN:
        for lines in readlines:
            if dtt in lines:
                print(dtt + " : Data Type Token")
    
def main():
    readFile()

if __name__ == "__main__":
    main()