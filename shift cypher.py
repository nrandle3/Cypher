# -*- coding: utf-8 -*-
# python3.7
"""
@author: nathan randle
"""

data = input("Please enter the data: ")
print()
for i in range(25):
    output = ""
    for char in data.lower():
        if not char.isalpha():
            output += char
        else:
            output += chr((ord(char) + i - 97) % 26 + 97)
    print(output + "\n")