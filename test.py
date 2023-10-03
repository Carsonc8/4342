# Instead of writing this massive Python code
# we can also code this in a different way

# Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import itertools
import sys
import os
# initializing strings for testing while putting them in an array
productList = ['chips', 'biscuits', 'pasta', 'cheese', 'bread', 'rice', 'honey', 'butter', 'cake', 'salt']
cowList = ['Chocolate', 'Strawberry', 'Vanilla', 'Coffee', 'dumbass']
keywords = ['if', 'then', 'program']

length = os.path.getsize("input.txt")
print(length)
with open ('inventory.txt'.replace(r'\n', '\n'), 'r') as f:
    readInLines = f.readlines()
    

"""
for key, keyss in itertools.zip_longest(productList, cowList):
    for line in readInLines:
        if key in line:
            print("found in PL")
        elif keyss in line:
            print("wow")

"""

for cows in cowList:
    for lines in readInLines:
        if cows in lines:
            print( cows + " was Found in CL ")
            flag = True
            
for product in productList:
    for lines in readInLines:
        if product in lines:
            print(product + " was found in product list")

for keyword in keywords:
    for lines in readInLines:
        if keyword in lines:
            print(keyword + " found in keyword")


if (readInLines) not in zip(productList, cowList, keywords):
    print(lines + " is not a valid identifier")
import string

# initializing empty list
test_list = []

# using string for filling alphabets
test_list = list(string.ascii_uppercase + string.ascii_lowercase)

# printing resultant list
print ("List after insertion : " + str(test_list))

            