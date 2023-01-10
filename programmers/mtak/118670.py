from collections import deque

def solution(rc,ops):
    rlen = len(rc)
    clen = len(rc[0])
    side_cols = [deque(rc[r][0] for r in range(rlen)), 
                 deque(rc[r][clen - 1] for r in range(rlen))]
    mid_rows = deque(deque(row[1:-1]) for row in rc)
    for op in ops:
        if op[0] == "S":
            mid_rows.appendleft(mid_rows.pop())
            side_cols[0].appendleft(side_cols[0].pop())
            side_cols[1].appendleft(side_cols[1].pop())
        else:
            mid_rows[rlen - 1].append(side_cols[1].pop())
            side_cols[0].append(mid_rows[rlen - 1].popleft())
            mid_rows[0].appendleft(side_cols[0].popleft())
            side_cols[1].appendleft(mid_rows[0].pop())
    ans = []
    for r in range(rlen):
        ans.append([])
        ans[r].append(side_cols[0][r])
        ans[r].extend(mid_rows[r])
        ans[r].append(side_cols[1][r])
    return ans