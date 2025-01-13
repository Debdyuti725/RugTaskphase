n=int(input("Enter number:"))
l=[]
c=0
m=n
while(m!=0):
    b=m%10
    l.append(b)
    m=m//10
l.reverse()
sum=0
for i in range(0,len(l)):
    if(i%2!=0):
        c=l[i]*2
        if(c>9):
            d=c
            s=0
            while(d!=0):
                b=d%10
                s=s+b
                d=d//10
            c=s
        l[i]=c
    sum=sum+l[i]
if(sum%10==0):
    print("Valid")
else:
    print("Not valid")


        

        




