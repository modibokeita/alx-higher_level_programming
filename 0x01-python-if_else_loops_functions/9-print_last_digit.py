#!/usr/bin/env python3
def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    print("{}".format(last_digit))

    return last_digit
