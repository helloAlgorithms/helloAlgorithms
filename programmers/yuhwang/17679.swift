func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    var answer = 0
    var map = board.map { Array($0).map { String($0) } }
    
    while true {
        var erase = Array(repeating: Array(repeating: false, count: n), count: m)
        
        for i in 0..<(m - 1) {
            for j in 0..<(n - 1) {
                guard map[i][j] != "" else { continue }
                if map[i][j] == map[i + 1][j] && map[i][j] == map[i][j + 1] && map[i][j] == map[i + 1][j + 1] {
                    erase[i][j] = true
                    erase[i + 1][j] = true
                    erase[i][j + 1] = true
                    erase[i + 1][j + 1] = true
                }
            }
        }
        for i in 0..<m {
            for j in 0..<n {
                if erase[i][j] {
                    map[i][j] = ""
                }
            }
        }
        var h = m - 1
        while h > 0 {
            for w in 0..<n {
                if map[h][w] == "" {
                    var c = h
                    while c >= 0 && map[c][w] == "" {
                        c -= 1
                    }
                    if c >= 0 {
                        map[h][w] = map[c][w]
                        map[c][w] = ""
                    }
                }
            }
            h -= 1
        }
        
        let erased = erase.reduce(0) { $0 + $1.filter { $0 }.count }
        if erased == 0 { break }
        answer += erased
    }
    return answer
}