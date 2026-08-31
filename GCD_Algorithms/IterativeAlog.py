import random
# find the greatest common denominator 
# a gets replaced by b in order to make the gcd input values as small ass possible 

def gcd_with_steps(a,b):
    iterations = 0

    while b != 0:
        r = a % b
        a = b
        b = r

        iterations += 1


    return abs(a), iterations

""" creates 10 random integers 1-10000, finds the gcd of them
then prints the random numbers, gcd, and iterations for each loop
"""

num = 1
total_steps = 0

""""" this is the random generator 
for _ in range(num):
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    g, var = gcd_with_steps(a, b)
    total_steps += var
"""

for _ in range(num):
    a = 1000
    b = 

    g, var = gcd_with_steps(a, b)
    total_steps += var

average = total_steps / num

print(something)

