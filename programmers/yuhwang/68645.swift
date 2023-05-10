import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = []
    var last = n * (n + 1) / 2
    var map: [[Int]] = []
    for i in 1...n {
        map.append(Array(repeating: 0, count: i))
    }
    var i = 1
    var y = 0
    var x = 0
    while i <= last {
        while y < map.count && map[y][x] == 0 {
            map[y][x] = i
            i += 1
            y += 1
        }
        y -= 1
        x += 1

        while x < map[y].count && map[y][x] == 0 {
            map[y][x] = i
            i += 1
            x += 1
        }
        x -= 2
        y -= 1

        while y >= 0 && x >= 0 && map[y][x] == 0 {
            map[y][x] = i
            i += 1
            x -= 1
            y -= 1
        }
        y += 2
        x += 1
    }
    return map.reduce(answer, +)
}
