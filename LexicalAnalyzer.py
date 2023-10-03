"""
Carson Cooper
CSCI4342_LexicalAnalazyer.py
Files used: input.txt
THe purpose of this progrma is to read in a file from the command line and decide what type of token it is.
"""
import sys
import string
IDENTIFIER_REGEX = list(string.ascii_uppercase + string.ascii_lowercase)
INTEGER_TOKENS = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
ADDITION_TOKEN = ['+','-','or',]
MULTIPLYING_TOKEN = ['*','div','and',]
SPECIAL_KEYWORD = ['program','var','procedure','begin','end','if','then','else','while','read', '(', ')', ':', ';', ',', '.']
ASSIGNMENT_OPERATOR = [':=',]
RELATIONAL_TOKEN = ['=','<>','<','<=','>=''>']
DATA_TYPE_TOKEN = ['integer','boolean','true','false']


#Reads in a file given by the command line and then goes through multiple for loops to decide what type of token it is 
def readFile(input_file):
    
    with open(input_file.replace('\n', '\n'), "r") as f:
        readlines = f.readlines()
    #Start of for loop and figuring out what type of token it is
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
    
#Takes the input file and gives it to the method readFile
def main():
    input_file = sys.argv[1]
    readFile(input_file)


if __name__ == "__main__":
    main()