#!/usr/bin/env python3

string = input("type a string: ")

def get_index(string, char):
  first_index = string.find(char)
  second_index = string.find(char, first_index+1)
  if (first_index < 0):
    return first_index + second_index
  else:
    return second_index


print(get_index(string, "f"))