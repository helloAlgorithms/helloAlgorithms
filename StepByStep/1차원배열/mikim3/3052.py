
arr=set()  # set() 으로 중복되는 요소를 제거     # 집합자료형은 중복되는 수를 하나로 본다.
for i in range(10): # 10번반복
    n=int(input())   # 한번씩 입력받을 수
    arr.add(n%42)
print(len(arr))
