def ssort(a):
    
    
    a=a.lower()
    s=[]
    for i in range(0,len(a)):
        if(a[i]!=' '):
            s.append(a[i])
    for i in range(0,len(s)-1):
        min=i
        for j in range(i+1,len(s)):
            if(s[min]>s[j]):
                min=j
        s[i],s[min]=s[min],s[i]
    
    return s

a=input("Enter string:")
b=input("Enter string:")
a=ssort(a)
b=ssort(b)
if(a==b):
    print("strings are anagram")
else:
    print("not anagram")