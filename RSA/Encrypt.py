# public key is m and e

e = int(input("What is e? "))
m = int(input("What is m? "))

message = int(input("What would you like to encrypt? "))

while message != -1 :
    encryptMsg = (message ** e) % m
    print(encryptMsg)
    message = int(input("What would you like to encrypt? "))


