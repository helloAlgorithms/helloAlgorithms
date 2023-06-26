import Foundation

func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    var answer = 0
    var comb: [[Int]] = []
    
    func recursive(_ now: Int, _ max: Int, _ arr: [Int]) {
        if now == max {
            comb.append(arr)
            return
        }
        var arr = arr
        for i in 0..<max {
            if arr.contains(i) { continue }
            arr.append(i)
            recursive(now + 1, max, arr)
            arr.popLast()
        }
    }
    recursive(0, dungeons.count, [])
    
    for order in comb {
        var k = k
        var clear = 0
        for d in order {
            if dungeons[d][0] > k { break }
            k -= dungeons[d][1]
            clear += 1
        }
        answer = max(answer, clear)
    }
    return answer
}