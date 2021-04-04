arr=[1,202,2,3,205,4,5]
#amount=[1,202,2,3,205,4,5]
#an=[1,203,3,6,408,10,15]
arr1=[402,202,2,3,205,4,5]
def maximumAmunt(arr):
    amount=[]
    lent=len(arr)
    for i in range(lent):
        amount.append(arr[i])
    for i in range(1,lent):
        for j in range(i):
            if arr[j]<arr[i]:
                if amount[j]+arr[i]>amount[i]:
                    amount[i]=amount[j]+arr[i]

    return max(amount)

print(maximumAmunt(arr))
print(maximumAmunt(arr1))