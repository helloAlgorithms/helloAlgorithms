def solution(arr1, arr2):
    answer = []
    
    n = len(arr2[0])
    for row1 in arr1:
        tmp = []
        for i in range(n):
            s = 0
            for j in range(len(row1)):
                s += row1[j] * arr2[j][i]
            tmp.append(s)
        answer.append(tmp)
                
    return answer
