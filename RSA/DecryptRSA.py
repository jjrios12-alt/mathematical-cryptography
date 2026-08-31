# p, q, and d private
# m and e are public 
# d and m and private 

d = int(input("What is d? "))
m = int(input("What is m? "))

encMsg = int(input("What would you like to Decrypt?"))

while encMsg != -1 :
    decryptMsg = (encMsg ** d) % m 
    print(decryptMsg)
    encMsg = int(input("What is your next number? (Enter -1 to quit) "))


