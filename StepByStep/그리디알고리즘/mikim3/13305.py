# 시작 10:15  10:45에 끝

# 키포인트
# 실제 거리를 움직일때 앞으로 얼마나 이 가격의 기름을 넣을지 계산하려고 했더니 복잡해졌다. 
# 그냥 최솟값을 기억해두고 그 값이 다른 최솟값을 만났을때 갱신되게끔 하니까 훨씬 쉬웠다.

n = int(input())
li_distance = list(map(int,input().split()))
li_cost = list(map(int,input().split()))
total_cost = 0

mini = li_cost[0]
for i in range(n-1):
    # 만약에 싼 도시를 만나면 최솟값 갱신
    if li_cost[i] < mini:
        mini = li_cost[i]
    total_cost += mini * li_distance[i]
    
print(total_cost)
