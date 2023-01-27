"""Write a Python function that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""




print("Enter words separated by Hyphens : ")
l = [w for w in input().split("-")]
l.sort()
print('-'.join(l))