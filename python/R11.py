s=input("enter a text:")
l=0
w=1
p=0
for i in range(0,len(s)):
    if(s[i]>'a' and s[i]<'z' or s[i]>'A' and s[i]<'Z' ):
        l=l+1
    if(s[i]==' '):
        w=w+1
    if(s[i]=='.'):
        p=p+1
t=0.0588*(l/w)*100.0-0.296*(p/w)*100.0-15.8
print(t)