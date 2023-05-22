import Foundation

func solution(_ nums:[Int]) -> Int {
    var answer = 0
    var prime = Array(2...3000)
    for i in 2...1500 {
        prime = prime.filter {
            if $0 == i { return true }
            else { return $0 % i != 0 }
        }
    }
    for i in 0..<(nums.count - 2) {
        for j in (i + 1)..<(nums.count - 1) {
            for k in (j + 1)..<(nums.count) {
                if prime.contains(nums[i] + nums[j] + nums[k]) {
                    answer += 1
                }
            }
        }
    }

    return answer
}
