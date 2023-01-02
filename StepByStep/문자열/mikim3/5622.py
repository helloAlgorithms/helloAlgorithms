# 5622 번 문제
# 다이얼 
# 너무 심하게 비효울적인 코드여서 지움 처음에는 딕셔너리로 풀었음

# 숫자값 더한거 +더한 숫자 갯수 만큼 소비?

### 제법 모범답안
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']  # 원하는 문자열을 원하는 인덱스에 넣고 list.index('원하는문자')으로 인덱스 값을 반환받을수 있다.
# dial.index('G')  # 'G'가 어디 있나 찾아서 인덱스값 반환 = 2
text = input().upper()
time = 0
for i in text:
    for j in dial:
        for k in j:
            if i == k:
                print("k=",k)
                print("j=",j)
                time += dial.index(j) + 3
print(time)
