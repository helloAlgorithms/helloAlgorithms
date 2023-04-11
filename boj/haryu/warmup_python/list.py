a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

n = 10
b = [0] * n
print(b)

print(a[0:2])

b = a[0:2] 

print(a)
print(b)

# list comprehension 

n = 2
m = 3

# 정상적인 리스트 컴프리헨션 방식의 배열  할당
arr = [[0] * m for _ in range(n)]
print(arr)

# 잘못된 리스트 컴프리헨션 방식의 배열 할당
arr2 = [[0]*m]*n
print(arr2)

# id() 는 메모리 주소는 아니지만 함수 객체의 고유한 식별자(메모리주소)를 반환해주므로, 확인시 arr2는 동일한 고유값을 가지는 것을 알 수 있다. 
# 한가지 특이한 것은 이렇게 할당시 리스트 내부에 값들은 동일한 아이디를 갖게 된다. 
print(id(arr[0][0]), " : ", arr[0][0])
print(id(arr[0][1]), " : ", arr[0][1])
print(id(arr[0][2]), " : ", arr[0][2])

# 이 경우에는 변수를 넣으면 고유 값이 변경된다. 즉 내부에서 레퍼런스로 동작한다는 것을 알 수 있다. 
arr[0][0] = 2
arr[0][1] = arr[0][0]
arr[0][2] = arr[0][1]


print(id(arr[0][0]), " : ", arr[0][0])
print(id(arr[0][1]), " : ", arr[0][1])
print(id(arr[0][2]), " : ", arr[0][2])


print(id(arr[1]))

print(id(arr2[0]))
print(id(arr2[1]))

# 언더바 사용 예시 

summary = 0
for i in range(0, 9):
    summary += i
print(summary)
