import Foundation

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    var s: [String: Int] = [:]
    
    func recursive(_ idx: Int, _ str: [Character], _ newStr: String) {
        if course.last! < newStr.count { return }
        
        if course.contains(newStr.count) {
            s[newStr, default: 0] += 1
        }
        
        for i in idx..<str.count {
            recursive(i + 1, str, newStr + String(str[i]))
        }
    }
    
    for order in orders {
        recursive(0, order.sorted(), "")
    }
    
    var result: [String] = []
    for len in course {
        let tmp = s.filter { $0.key.count == len && $0.value > 1 }
        let m = tmp.max { $0.value < $1.value }
        let menu = tmp.filter { m!.value == $0.value }.map { $0.key }
        result.append(contentsOf: menu)
    }
    return result.sorted()
}