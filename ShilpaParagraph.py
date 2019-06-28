import os
import csv
import re



# Store the file path associated with the file (note the backslash may be OS specific)
file = "/Users/muralipremkumar/Desktop/RICE_DATA/RICEHOU201906DATA1/HW/03-Python/ExtraContent/Instructions/PyParagraph/raw_data/paragraph_1.txt"

# Variables
lines = 0
nwords = 0
nchar = 0
sentences = 0
alphacount = 0

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as f:

    for line in f:
        for char in line:
            if char.isalpha() == True:
                alphacount = alphacount + 1
        words = line.split()
        print(words)
        nwords += len(words)
        lines += 1
        nchar += len(line)

     # assume that each sentence ends with . or ! or ?
    # so simply count these characters
    sentences += line.count('.') + line.count('!') + line.count('?')


    print("----------------------------------------------------------------")
    print("Paragraph Analysis")
    print("----------------------------------------------------------------")
    print("Number of words :", nwords)
    print("Numbers of characters:", nchar)
    print("Number of sentences:", sentences)
    print("Number of letters:", alphacount)
    print("Average letter count per word =", alphacount / nwords)
    print("Average sentence length = ", nwords / sentences)
    print("----------------------------------------------------------------")