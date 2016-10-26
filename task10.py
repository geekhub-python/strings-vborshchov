#!/usr/bin/env python3

string = 'Loremh H 11 h 2h2h 3h3h hipsuhm'

print("Given string is:\n\n%s" % string)
print("\n")

first_index = string.find("h")
last_index = string.rfind("h")

result = string[:first_index] + string[last_index+1:]

print(result)
