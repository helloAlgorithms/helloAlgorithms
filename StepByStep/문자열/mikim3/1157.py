
# ***********내가 자주봐야할 문제 
# 답지보고 다른 방법으로 풀음

a=input()
a.count('i')
a=a.upper()
# max=0  #  키워드를 변수로 쓰지말자!!!!!!!!!!
arr=[]
for i in range(26):  # 알파벳 갯수만큼 반복
    # arr[i]=a.count(chr(i+97))   # A의 갯수부터 시작  # !!! *append를 습관적으로 쓰자 !!!
    arr.append(a.count(chr(i+65)))   # A의 갯수부터 시작
dict_1=dict()
for i in range(26):
    dict_1[chr(i+65)]=arr[i]
max_key= max(dict_1,key=dict_1.get)    # 최대값을 max로 찾아내기    최대값이 여러개여도 하나만 출력
print(max_key)
licompri=[k for k,v in dict_1.items() if max(dict_1.values())==v]   # 최대값이 여러개면 여러개 다 출력
if len(licompri)>1:
    print("?")
else:
    print(licompri[0])