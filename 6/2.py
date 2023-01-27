"""Write a Python function that checks whether a passed string is palindrome or not. Note:
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run."""
def p(s):
    return s == s[::-1]
s = input("please enter your word ")
ans = p(s)
if ans:
    print("Yes")
else:
    print("No")