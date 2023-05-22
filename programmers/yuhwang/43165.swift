import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var answer = 0
    func dfs(_ idx: Int, _ sum: Int) {
        if idx == numbers.count {
            if sum == target { answer += 1 }
            return
        }
        dfs(idx + 1, sum + numbers[idx])
        dfs(idx + 1, sum - numbers[idx])
    }
    dfs(0, 0)
    return answer
}
