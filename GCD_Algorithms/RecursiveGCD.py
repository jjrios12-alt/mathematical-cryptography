a = int(input("What is a? "))
b = int(input("What is b? "))


# identical to the mathematical representation of a gcd
# gcd(a,b) { 
def gcd_recursive(a,b) :
    if b == 0 :
        return abs(a)

    return gcd_recursive(b, a % b)

print(gcd_recursive(a, b))