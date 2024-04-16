#!/bin/python3
import string # This module might be useful.

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Code part 1 functions here:
def alphabet_function(x):
  input = x.lower()
  index = alph.index(input)
  return index 
  
def shift_character(char, shift):
  if char.islower():
    index = alph.index(char) + shift
    if index >= 26: #keeps index within range
      index %= 26
    return alph[index]
  elif char.isupper():
    index = alphUpper.index(char) + shift
    if index >= 26: #keeps index within range
      index %= 26
    return alphUpper[index]
  else:
    return char

def build_code_dict(int):
  newAlph = []
  newAlphUpper = []
  for i in alph:
    newAlph.append(shift_character(i, int))
  for i in alphUpper:
    newAlphUpper.append(shift_character(i, int))
  cypher = dict(zip(alph, newAlph))
  upperCypher = dict(zip(alphUpper, newAlphUpper))
  cypher.update(upperCypher)
  return cypher
  
def encrypt_with_shift(text, shift = 1):
  shifted_dict = build_code_dict(shift)
  coded_message = ""
  for char in text:
    if char in shifted_dict:
      coded_message += shifted_dict[char]
    else:
      coded_message += char
  return coded_message
  
def decrypt(text, shift):
  decrypted_message = encrypt_with_shift(text, shift)
  return decrypted_message