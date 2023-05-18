import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var budget = budget
    var answer = 0
    for i in d.sorted() {
        if budget < i { return answer }
        budget -= i
        answer += 1
    }
    return answer
}
