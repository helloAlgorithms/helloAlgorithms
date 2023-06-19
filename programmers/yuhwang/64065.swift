import Foundation

func solution(_ s:String) -> [Int] {
    var answer: [Int] = []
    var s = s
    s.removeFirst(2)
    s.removeLast(2)
    var arr: [Set<Int>] = s.components(separatedBy: "},{").map {
        Set($0.split(separator: ",").map { Int(String($0))! })
    }.sorted { $0.count < $1.count}
    
    answer.append(arr[0].first!)
    for i in 1..<arr.count {
        answer.append(arr[i].subtracting(arr[i - 1]).first!)
    }
    return answer
}