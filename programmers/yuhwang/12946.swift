import Foundation

func solution(_ n:Int) -> [[Int]] {
    var answer: [[Int]] = []

    func hanoi(_ n: Int, _ from: Int, _ to: Int) {
        if n == 1 {
            answer.append([from, to])
            return
        }
        hanoi(n - 1, from, 6 - from - to)
        answer.append([from, to])
        hanoi(n - 1, 6 - from - to, to)
    }

    hanoi(n, 1, 3)
    return answer
}
