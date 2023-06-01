import Foundation

var dict: [String: Int] = ["A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26]

func solution(_ msg: String) -> [Int] {
    let msg = Array(msg)
    let len = msg.count
    
    var dictIndex = 27
    var result: [Int] = []
    
    var i = 0
    
    while i < len {
        var current = "\(msg[i])"
        
        while true {
            if dict[current] != nil {
                i += 1
                
                if i == len {
                    result.append(dict[current]!)
                    break
                }
                
                current.append(msg[i])
            } else {
                dict[current] = dictIndex
                dictIndex += 1
                current.removeLast()
                result.append(dict[current]!)
                break
            }
        }
    }
    
    return result
}