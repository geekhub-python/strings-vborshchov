#!/usr/bin/env python3

string = 'Lorem ipsum dolor sit amet'
print("Given string is:\n\n%s" % string)
print("\n")

print("1. Third symbol is '%s'" % string[2])

print("2. Second symbol from end is '%s'" % string[-2])

print("3. First five symbols are '%s'" % string[:5])

print("4. All string except two last symblos is '%s'" % string[:-2])

print("5. The length of a string is %s" % len(string))

print("6. All symbols with even indexes are '%s'" % string[::2])

print("7. All symbols with odd indexes are '%s'" % (string)[1::2])

print("8. Reverse string is '%s'" % string[::-1])

print("9. Reverse string with every second symbol is '%s'" % string[::-1][::2])
