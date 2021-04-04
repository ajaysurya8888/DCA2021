def productnum(n):
    prod=1
    while n!=0:
        dig=n%10
        prod=prod*dig
        n=n//10
    return prod

print(productnum(32))
print(productnum(45))
print(productnum(10))