#!/usr/bin/env python3

string = input("type a string: ")

def get_indices(string):
  result = ""
  for index, char in enumerate(string):
    if (index % 3 == 0):
      result += char
  return result

print(get_indices(string))