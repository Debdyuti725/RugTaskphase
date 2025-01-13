def fact(n):
    if(n==0):
        return 1
    if(n==1):
        return 1

    p=n*fact(n-1) #n!=n*(n-1)!
    return p
    
a=int(input("Enter number:"))
print(fact(a))