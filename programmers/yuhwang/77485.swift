import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = []
    var map: [[Int]] = Array(repeating: Array(repeating: 0, count: columns + 1), count: rows + 1)
    for i in 1...rows {
        for j in 1...columns {
            map[i][j] = (i - 1) * columns + j
        }
    }
    
    // [x1, y1, x2, y2]
    for query in queries {
        var point: (x: Int, y: Int) = (query[0], query[1])
        var m = map[point.x][point.y]
        var old = map[point.x + 1][point.y]
        
        while point.y < query[3] {
            let t = map[point.x][point.y]
            m = min(m, t)
            
            map[point.x][point.y] = old
            old = t
            
            point.y += 1
        }
        
        while point.x < query[2] {
            let t = map[point.x][point.y]
            m = min(m, t)
            
            map[point.x][point.y] = old
            old = t
            
            point.x += 1
        }
        
        while point.y > query[1] {
            let t = map[point.x][point.y]
            m = min(m, t)
            
            map[point.x][point.y] = old
            old = t
            
            point.y -= 1
        }
        
        while point.x > query[0] {
            let t = map[point.x][point.y]
            m = min(m, t)
            
            map[point.x][point.y] = old
            old = t
            
            point.x -= 1
        }
        
        answer.append(m)
    }
    return answer
}