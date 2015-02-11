#!/usr/bin/env python
import hashlib


def main():
  input = raw_input("Enter input: ")
  m = hashlib.md5()
  m.update(input)
  print m.hexdigest()

if __name__ == '__main__':
   main()

