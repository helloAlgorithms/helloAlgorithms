import Foundation

func solution(_ k:Int, _ d:Int) -> Int64 {
    var answer: Int64 = 0
    var r = d
    var i = 0
    while i <= d {
        while i * i + r * r > d * d {
            r -= 1
        }
        answer += Int64(r / k + 1)
        i += k
    }
    return answer
}