
p = int(input("What is p? (Must be prime) "))
q = int(input("What is q? (Must be prime) "))

m = p * q

phi_m = (p-1) * (q-1)

print("phi_m = ", phi_m)
e = int(input("What is e? (Must be relitively prime to phi_m)"))

m = p * q

d = 0

for i in range(1, phi_m):
    if (i * e) % phi_m == 1 :
        d = i
        break
print("m = ", m)
print("phi_m = ", phi_m)
print("d = ", d)

print("Public key: (", e, ",", m, ") ")
print("Private key: (", d, ",", m, ") ") 