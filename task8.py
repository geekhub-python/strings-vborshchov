#!/usr/bin/env python3

string = input("type a string: ")

def get_indices(string, char):
  indices = []
  indices.append(string.find(char))
  indices.append(string.rfind(char))
  indices = filter(lambda x: x >= 0, indices)
  result = list(set(indices))
  if (len(result) > 0):
    print(result)


get_indices(string, "f")