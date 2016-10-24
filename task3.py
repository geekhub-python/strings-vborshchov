#!/usr/bin/env python3

string = 'Lorem ipsum dolor sit amets'

print("Given string is:\n\n%s" % string)
print("\n")

left_length = (len(string) +1) // 2
left, right = string[:left_length], string[left_length:]

print(right + left)
