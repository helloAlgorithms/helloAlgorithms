arr=[]
ma=0
maxIndex=0
for i in range(9):
    arr.append(int(input()))
for i in range(9):
    if arr[i]>ma:
        maxIndex=i+1
        ma=arr[i]
print(ma)
print(maxIndex)