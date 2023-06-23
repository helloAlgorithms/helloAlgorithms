import Foundation

func solution(_ info:[String], _ query:[String]) -> [Int] {
    var answer: [Int] = []
    var comb: [String: [Int]] = [:]
    
    for lang in ["cpp", "java", "python", "-"] {
        for job in ["backend", "frontend", "-"] {
            for career in ["junior", "senior", "-"] {
                for soul in ["chicken", "pizza", "-"] {
                    comb[lang + job + career + soul] = []
                }
            }
        }
    }
    
    for info in info {
        let i = info.split(separator: " ").map { String($0) }
        for lang in [i[0], "-"] {
            for job in [i[1], "-"] {
                for career in [i[2], "-"] {
                    for soul in [i[3], "-"] {
                        comb[lang + job + career + soul]!.append(Int(i[4])!)
                    }
                }
            }
        }
    }
    
    for (key, value) in comb {
        comb[key] = value.sorted()
    }
    
    func lowerbound(_ arr: [Int], _ target: Int) -> Int {
        var start = 0
        var end = arr.count
        while start < end {
            let mid = (start + end) / 2
            if arr[mid] < target {
                start = mid + 1
            } else {
                end = mid
            }
        }
        return end
    }
    
    for q in query {
        let q = q.split(separator: " ").map { String($0) }
        answer.append(comb[q[0] + q[2] + q[4] + q[6]]!.count - lowerbound(comb[q[0] + q[2] + q[4] + q[6]]!, Int(q[7])!))
    }
    return answer
}