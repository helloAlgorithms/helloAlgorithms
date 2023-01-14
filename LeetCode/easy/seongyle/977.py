def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)

# 동적자료형을 쓸 때는 자료형을 큐와 덱중 어떤걸 쓸지 고민 후 사용
# 만약 길이를 이미 알고 있다면 정적배열로 하는 방법도 있음