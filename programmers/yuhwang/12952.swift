import Foundation

func solution(_ n:Int) -> Int {
    var map = Array(repeating: 0, count: n)
    var answer = 0

    func valid(_ idx: Int) -> Bool {
        for x in 0..<idx {
            if map[x] == map[idx] { return false }
            if abs(idx - x) == abs(map[idx] - map[x]) { return false }
        }
        return true
    }

    func nqueen(_ idx: Int) {
        if idx == n {
            answer += 1
            return
        }
        for i in 0..<n {
            map[idx] = i
            if valid(idx) {
                nqueen(idx + 1)
            }
            map[idx] = 0
        }
    }
    nqueen(0)
    return answer
}
