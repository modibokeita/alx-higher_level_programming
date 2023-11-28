#!/usr/bin/python3
def uppercase(s):
    str_char = str(s)
    for char in str_char:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}\n".format(upper_char), end="")
        else:
             print("{}\n".format(char), end="")
