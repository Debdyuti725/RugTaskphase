n=int(input("Enter number:"))
l=[]
while(n!=0):
    b=n%10
    l.append(b)
    n=n/10
l.reverse()
for i in range(0,len(l)-1):
    
    if(l[i]>l[i+1]):
        
        for j in range(i+1,len(l)-1):
            if(l[j]<l[j+1]):
                print("not a hill number")
                exit(0)
print("it is a hill number")
            
