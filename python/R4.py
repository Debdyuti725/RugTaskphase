def ssort(a):
    s=[]
    for i in range(0,len(a)):
        s.append(a[i])
    for i in range(0,len(s)-1):
        min=i
        for j in range(i+1,len(s)):
            if(s[min]>s[j]):
                min=j
        s[i],s[min]=s[min],s[i]
    print(" ".join(s))
    
s=input("Enter string:")
ssort(s)