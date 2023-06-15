import Foundation

func solution(_ relation:[[String]]) -> Int {
    var candidates: [[Int]] = []
    
    func recursive(_ now: Int, _ last: Int, _ tmp: [Int]) {
        if now == last { return }
        
        var tmp = tmp
        for i in now..<last {
            tmp.append(i)
            candidates.append(tmp)
            recursive(i + 1, last, tmp)
            _ = tmp.popLast()
        }
    }
    recursive(0, relation[0].count, [])
    candidates.sort { $0.count < $1.count }
    
    func isUnique(_ attributes: [Int]) -> Bool {
        var attr: Set<String> = Set<String>()
        
        for i in 0..<relation.count {
            var sum: String = ""
            for a in attributes {
                sum += relation[i][a]
                sum += " "
            }
            attr.insert(sum)
        }
        return attr.count == relation.count
    }
    
    var idx = 0
    while idx < candidates.count {
        if !isUnique(candidates[idx]) {
            candidates.remove(at: idx)
            continue
        } else {
            candidates = candidates.filter {
                if $0 == candidates[idx] { return true }
                var count = candidates[idx].count
                for i in $0 {
                    if candidates[idx].contains(i) {
                        count -= 1
                    }
                }
                return count != 0
            }
        }
        idx += 1
    }

    return candidates.count
}