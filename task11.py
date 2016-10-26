#!/usr/bin/env python3

string = 'Loremh123456789hm'

print("Given string is:\n\n%s" % string)
print("\n")

first_index = string.find("h")
last_index = string.rfind("h")

result = string[:first_index] + string[first_index+1:last_index+1][::-1] + string[last_index:]

print(result)
