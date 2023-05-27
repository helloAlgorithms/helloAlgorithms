import Foundation

func solution(_ land:[[Int]]) -> Int {
    var map = Array(repeating: Array(repeating: 0, count: 4), count: land.count)
    map[0] = land[0]
    for row in 1..<map.count {
        for i in 0..<4 {
            var m = 0
            for j in 0..<4 {
                if j == i { continue }
                m = max(m, map[row - 1][j])
            }
            map[row][i] = m + land[row][i]
        }
    }
    return map.last!.sorted()[3]
}
