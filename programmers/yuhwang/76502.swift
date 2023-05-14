import Foundation

func solution(_ s:String) -> Int {
    var answer = 0
    var str = s
    if s.count % 2 != 0 { return 0 }

    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        for c in s {
            if stack.isEmpty {
                stack.append(c)
                continue
            }
            if stack.last! == "[" && c == "]" {
                stack.removeLast()
                continue
            }
            if stack.last! == "{" && c == "}" {
                stack.removeLast()
                continue
            }
            if stack.last! == "(" && c == ")" {
                stack.removeLast()
                continue
            }
            stack.append(c)
        }
        return stack.isEmpty ? true : false
    }
    for i in 0..<(s.count - 1) {
        if isValid(str) { break }
        str.append(str.first!)
        str.removeFirst()
    }
    var stack: [Character] = []
    for c in str {
        if stack.isEmpty {
            stack.append(c)
            continue
        }
        if stack.last! == "[" && c == "]" {
            stack.removeLast()
            if stack.count == 0 { answer += 1 }
            continue
        }
        if stack.last! == "{" && c == "}" {
            stack.removeLast()
            if stack.count == 0 { answer += 1 }
            continue
        }
        if stack.last! == "(" && c == ")" {
            stack.removeLast()
            if stack.count == 0 { answer += 1 }
            continue
        }
        stack.append(c)
    }
    return answer
}
