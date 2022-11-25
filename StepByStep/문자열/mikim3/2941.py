# 2941 번 문제
# 크로아티아 알파벳
# 너무 오래걸림

# ljes=njak  lj e s= nj a k
a=["c=","c-","d-","lj","nj","s=","z="]  # 두글자 비교할꺼
b=["dz="]  # 3글자 비교할꺼

m=input()  # 입력
count=0
if len(m)==1:
    count=1
else:
    for i in range(len(m)-2):
        # print(i)
        if m[i]+m[i+1] in a:
            # print("m[i]+m[i+1]",m[i]+m[i+1])
            count-=1
        elif m[i]+m[i+1]+m[i+2] in b:
            # print("m[i]+m[i+1]+m[i+2]",m[i]+m[i+1]+m[i+2])
            count-=1  # z= 에서 한번 더걸려서 1만빼기  총 2가 빠짐
        count+=1
    if m[-2]+m[-1] in a:
        # print("m[-2]+m[-1]",m[-2]+m[-1])
        count-=1
    count+=2 # 끝에 두개 안샌거 더하기
print(count)