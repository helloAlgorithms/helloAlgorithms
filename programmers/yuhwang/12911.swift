import Foundation

func solution(_ n:Int) -> Int {
    var answer = n + 1
    while true {
        if String(answer, radix: 2).filter { $0 == "1" }.count == String(n, radix: 2).filter { $0 == "1" }.count {
            return answer
        }
        answer += 1
    }
}
