import Foundation

func solution(_ topping:[Int]) -> Int {
    var answer = 0
    var front: [Int: Int] = [:]
    for i in topping {
        front[i] = (front[i] ?? 0) + 1
    }
    var back: [Int: Int] = [:]
    for i in topping.reversed() {
        back[i] = (back[i] ?? 0) + 1
        front[i] = front[i]! - 1
        if front[i]! == 0 {
            front.removeValue(forKey: i)
        }
        if back.count == front.count { answer += 1 }
    }

    return answer
}
