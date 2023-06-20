import Foundation

func solution(_ expression:String) -> Int64 {
    let oper: [[String]] = [["+", "-", "*"], ["+", "*", "-"], ["-", "+", "*"], ["-", "*", "+"], ["*", "-", "+"], ["*", "+", "-"]]
    var str = expression
    var arr: [String] = []
    var tmp = ""
    while str.count > 0 {
        let c = str.popLast()!
        if c.isNumber {
            tmp = String(c) + tmp
        } else {
            arr.append(tmp)
            tmp = ""
            arr.append(String(c))
        }
    }
    arr.append(tmp)
    var answer: Int64 = 0
    
    for i in 0..<6 {
        var array = Array(arr.reversed())
        var stack: [String] = []
        for j in 0..<3 {
            for s in array {
                if (stack.last ?? "") == oper[i][j] {
                    switch stack.popLast()! {
                    case "*":
                        stack.append(String(Int64(stack.popLast()!)! * Int64(s)!))
                    case "+":
                        stack.append(String(Int64(stack.popLast()!)! + Int64(s)!))
                    case "-":
                        stack.append(String(Int64(stack.popLast()!)! - Int64(s)!))
                    default:
                        break
                    }
                } else {
                    stack.append(s)
                }
            }
            array = stack
            stack = []
        }
        answer = max(abs(Int64(array[0])!), answer)
    }
    return answer
}