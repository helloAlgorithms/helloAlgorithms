# 알파벳 찾기
# 답지보았지만 다시 내 방법으로 품
# ord() 의 반대는 chr() 이라는 것을 몰랐음

a=input()
i='a'  # 97   ord('a')  # 97
# 
a.find('a')  #이러면 a 위치는 나옴
a.find('b')
for i in range(26):
    print(a.find(chr(i+97)),end=' ')