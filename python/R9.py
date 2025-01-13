s=input("Enter string:")
t=int(input("Enter shift:"))
d=""
for i in range(0,len(s)):
    a=ord(s[i])
    a=a+t
    if(a>90 and a<97 ):
        a=64+(a-90)
    elif(a>122):
        a=96+(a-122)
    
    c=chr(a)
    d=d+c
print(d)