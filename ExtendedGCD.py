


def gcd_with_steps(a,b):

    while b != 0:
        r = a % b
        a = b
        b = r

    return r, a, b



    return abs(a) 

g, x, y = extended_gcd(252, 105)