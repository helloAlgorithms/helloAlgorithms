import Foundation

func solution(_ N:Int, _ road:[[Int]], _ k:Int) -> Int {
    var cost = Array(repeating: Int.max, count: N + 1)
    var map = Array(repeating: Array(repeating: Int.max, count: N + 1), count: N + 1)
    cost[1] = 0
    
    for r in road {
        map[r[0]][r[1]] = min(r[2], map[r[0]][r[1]])
        map[r[1]][r[0]] = min(r[2], map[r[1]][r[0]])
    }
    
    var q: [(idx: Int, cost: Int)] = [(1, 0)]
    var idx = 0
    
    while idx < q.count {
        let cur = q[idx]
        idx += 1
        
        for i in 1...N {
            if map[cur.idx][i] == Int.max { continue }
            
            let newCost = cur.cost + map[cur.idx][i]
            if newCost < cost[i] {
                cost[i] = min(cost[i], newCost)
                q.append((i, newCost))
            }
        }
    }

    return cost.filter { $0 <= k }.count
}