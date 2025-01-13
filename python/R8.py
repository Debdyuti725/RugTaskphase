a=input("Enter string:")

n=0


for i in range(2,len(a)+1):
    b=a[0:i]
    
    c=a[i:i+i]
    
    if(b==c):
        
        n=i-1
        break

if(n==0):
    print("no repeating sequence")
    exit(0)


for i in range(0,len(a),n+1):
    c=(a[i:n+1+i])
    print(c,end=",")