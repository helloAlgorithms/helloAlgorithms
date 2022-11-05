x=int(input())
y=int(input())
saboon=0
if x>0 and y>0:
    saboon=1
elif x<0 and y>0:
    saboon=2
elif x<0 and y<0:
    saboon=3    
else:
    saboon=4
print(saboon)