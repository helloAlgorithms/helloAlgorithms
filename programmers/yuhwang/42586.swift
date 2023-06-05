import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer: [Int] = []
    var start = 0
    var progresses = progresses
    while start < progresses.count {
        for i in 0..<progresses.count {
            progresses[i] += speeds[i]
        }
        var done = 0
        while start < progresses.count && progresses[start] >= 100 {
            start += 1
            done += 1
        }
        if done > 0 {
            answer.append(done)
        }
    }
    return answer
}