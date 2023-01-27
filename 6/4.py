"""Write a Python function to check whether a string is a pangram or not. Note: Pangrams
are words or sentences containing every letter of the alphabet at least once. For
example: "The quick brown fox jumps over the lazy dog"""
import string
 
def a(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True

k = input("please enter your string ")
if(a(k) == True):
    print("Yes")
else:
    print("No")