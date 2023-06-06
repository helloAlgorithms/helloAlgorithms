import Foundation

func solution(_ citations:[Int]) -> Int {
    var i = citations.count
    while i > 0 {
        if citations.filter { $0 >= i }.count >= i {
            break
        }
        i -= 1
    }
    return i
}