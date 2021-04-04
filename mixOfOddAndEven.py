#sequence=[0,0,2,1,4,3,6,5,8,7,10,9,12,11,14,13,16,15,18,17,20,19,22,21,24,23,26,25]
#position=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

def nthnum(n):
    if n==0 or n==1:
        return 0
    if n%2!=0:
        return n-1
    else:
        return n-3


print(nthnum(10))
print(nthnum(20))
