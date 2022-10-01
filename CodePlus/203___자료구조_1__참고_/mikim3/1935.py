# 시작시간 0906   끝난시간 0941
# 답봄
# 문제를 보고 스택을 이용한다는 것은 알아챘지만 

# 키포인트
# stack = [] 로 숫자만 따로 모아두고 그 숫자를 str1 = stack.pop() str2 = stack.pop()으로
# 두가지변수로 분리해서 저장한게 키포인트다.

# 두번째로 ord(i) - ord('A')로 알파벳의 순서를 알아낸것도 키포인트다.

n = int(input())

word = input()
# 피연산자 값을 저장하기 위한 lst
num_lst = [0] * n 

for i in range(n):
    num_lst[i] = int(input())

# 리스트를 통해 후위표기식 계산
stack = []

for i in word:
    if 'A' <= i <= 'Z': # 후위표기식에서 알파벳을 만나면 stack에 저장
        stack.append(num_lst[ord(i) - ord('A')])
    else:
        print("stack ==",stack)
        str2 = stack.pop()
        str1 = stack.pop()
        
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
        print("str1 ==",str1,"   str2==",str2)
            
print('%.2f'%stack[0])
            



