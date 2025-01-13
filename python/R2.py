s=input("Enter string:");
for i in range(0,len(s)):
    a=s.count(s[i])
    print("count of",s[i]," is",a)

l=[]
for i in range(0,len(s)):
    l.append(s[i])

for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if(l[i]>l[j] and l[i]!=' ' and l[j]!=' '):
            l[i],l[j]=l[j],l[i]

print(" ".join(l))


    