#!/bin/python3
import random

chars ='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ?!.,-'
number = input ('number of passwords?')
length = input ('pasword length?')
length = int(length)
number = int(number)
for p in range (number):
  password = ''
  for c in range (length):
    password += random.choice(chars)
  print(password)