#!/usr/bin/env python3

string = 'Lhoremh H 11 h 2h2h 3h3h hipsuhm'

print("Given string is:\n\n%s" % string)
print("\n")

last_index = string.rfind("h")

result = string.replace('h', 'H')
result = result.replace('H', 'h', 1)
result = result[:last_index] + 'h' + result[last_index+1:]

# result = result[:first_index].replace('H', 'h') + result[first_index:]
# result = result[:last_index].replace('H', 'h') + result[last_index:]

print(result)
