def triple_and(a,b,c):
    if(a==True and c==True and b==True):
        return True
    else:
        return False

a=bool(input())
b=bool(input())
c=bool(input())
t=triple_and(a,b,c)
print(t)