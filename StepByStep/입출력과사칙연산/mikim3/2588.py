a=int(input())
b=int(input())
c=str(b)
for i in range(len(c)-1,-1,-1):
    print(a*int(c[i]))    
print(a*b)
