def  removeNum(si):
    s=list(si)
    lent=len(s)
    i=0
    ans=""
    while i<lent:
        if s[i].isdigit():
            if s[i]=="7":
                i=i+1
            elif s[i]=="5" and i+1<lent:
                if s[i+1]=="7":
                    i+=2
                else:
                    ans=ans+s[i]
                    i+=1
            else:
                ans=ans+s[i]
                i+=1
        else:
            ans = ans + s[i]
            i += 1
    return ans


print(removeNum("5577"))