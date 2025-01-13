a=input("Enter string:")

s=""


for i in range(0,len(a)):
    s=a[i]+s
l=len(s)
for i in range(0,len(a)):
    if(s[0]==a[i]):
        n=i
        break


    
for i in range(0,len(a),n+1):
    c=(a[i:n+1+i])
    print(c,end=",")

