triangles = []
end = [0, 0, 0]
while end not in triangles:
    triangles.append(list(map(int, input().split(' '))))
for index, item in enumerate(triangles):
    if index == (len(triangles) - 1):
        break ;
    isTri = 0
    isTri |= ((item[0]**2 + item[1]**2) == item[2]**2)
    isTri |= ((item[0]**2 + item[2]**2) == item[1]**2)
    isTri |= ((item[1]**2 + item[2]**2) == item[0]**2)
    print("right" if isTri & True else "wrong")
