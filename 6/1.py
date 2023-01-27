"""Write a Python function to check whether a number is perfect or not. According to
Wikipedia : In number theory, a perfect number is a positive integer that is equal to the
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the
number itself (also known as its aliquot sum). Equivalently, a perfect number is a
number that is half the sum of all of its positive divisors (including itself)."""

def is_perfect(n):
    m = 0
    for i in range(1,n):
        if n%i==0:
            m += i
    return m == n

number = int(input('Enter number: '))

if is_perfect(number):
    print('yes the number is perfect')
else:
    print('no the number is not perfect')