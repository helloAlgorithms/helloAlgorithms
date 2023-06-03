import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var cloth: [String: Int] = [:]
    for c in clothes {
        cloth[c[1], default: 0] += 1
    }

    var answer = 1
    for c in cloth {
        answer *= c.value + 1
    }
    return answer - 1
}