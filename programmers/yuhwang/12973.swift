import Foundation

func solution(_ s:String) -> Int {
    var arr: [Character] = []
    for c in s {
        if arr.isEmpty {
            arr.append(c)
            continue
        }
        if c == arr.last! {
            _ = arr.popLast()
        } else {
            arr.append(c)
        }
    }
    return arr.isEmpty ? 1 : 0
}
