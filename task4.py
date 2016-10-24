#!/usr/bin/env python3

string = 'Lorem ipsum'

print("Given string is:\n\n%s" % string)
print("\n")

parts = string.split(" ")
result = " ".join(parts[::-1])

print(result)
