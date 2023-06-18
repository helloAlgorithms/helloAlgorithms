import Foundation

func solution(_ p:String) -> String {
    if p == "" { return "" }
    
    var l = 0
    var r = 0
    for c in p {
        if c == "(" { l += 1 }
        else { r += 1}
        if l == r { break }
    }
    var u = String(p[p.startIndex..<p.index(p.startIndex, offsetBy: l + r)])
    var v = String(p[p.index(p.startIndex, offsetBy: l + r)...])
    if isValid(u) {
        return u + solution(v)
    }
    _ = u.removeFirst()
    _ = u.removeLast()
    
    return "(" + solution(v) + ")" + u.map {
        if $0 == "(" { return ")" }
        else { return "(" }
    }
}

func isValid(_ u: String) -> Bool {
    var stack: [Character] = []
    for c in u {
        if c == "(" { stack.append(c) }
        else if stack.isEmpty {
            return false
        } else {
            _ = stack.popLast()
        }
    }
    return stack.isEmpty
}