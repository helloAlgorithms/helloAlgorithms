import Foundation

func solution(_ s:String) -> [Int] {
    var removed = 0
    var count = 0
    var str = s
    while str.count > 1 {
        var nonzero = str.filter { $0 == "1" }.count
        removed += str.count - nonzero
        str = String(nonzero, radix: 2)
        count += 1
    }
    return [count, removed]
}
