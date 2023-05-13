import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var counts: [Int: Int] = [:]
    var K = tangerine.count - k
    for i in tangerine {
        if let c = counts[i] {
            counts[i] = c + 1
        } else {
            counts[i] = 1
        }
    }
    let count = Array(counts).sorted { $0.value < $1.value }
    var idx = 0
    while K > 0 {
        if K >= count[idx].value {
            K -= count[idx].value
            idx += 1
        } else {
            K = 0
            break
        }
    }
    return count.count - idx
}
