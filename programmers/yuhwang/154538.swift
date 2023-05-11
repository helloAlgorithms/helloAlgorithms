import Foundation

func solution(_ x:Int, _ y:Int, _ n:Int) -> Int {
    var map = Array(repeating: Int.max, count: y + 1)
    map[x] = 0
    for i in x...y {
        if n < i && map[i - n] != Int.max {
            map[i] = min(map[i], map[i - n] + 1)
        }
        if i % 2 == 0 && map[i / 2] != Int.max {
            map[i] = min(map[i], map[i / 2] + 1)
        }
        if i % 3 == 0 && map[i / 3] != Int.max {
            map[i] = min(map[i], map[i / 3] + 1)
        }
    }
    return map[y] == Int.max ? -1 : map[y]
}
