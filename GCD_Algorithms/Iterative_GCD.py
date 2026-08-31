import random
# find the greatest common denominator 
# a gets replaced by b in order to make the gcd input values as small ass possible 

def gcd_with_steps(a,b):
    iterations = 0

    while b != 0:
        r = a % b
        print(a, "%", b, "=", r)
        a = b
        b = r

        iterations += 1


    return abs(a), iterations

""" creates 10 random integers 1-10000, finds the gcd of them
then prints the random numbers, gcd, and iterations for each loop
"""

num = 1
total_steps = 0
a = int(input("What is a? "))
b = int(input("What is b? "))

g, steps = gcd_with_steps(a,b)
print("gcd of a and b is : ", g)
print("Steps of a and b : ", steps)


print("Testing GitHub update")