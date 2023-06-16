import Foundation

func solution(_ s:String) -> Int {
    var answer = s.count
    let str = s.map { String($0) }
    if s.count == 1 {
        return 1
    }
    
    for i in 1...s.count/2 {
        var tmp = ""
        
        var j = 0
        while j < s.count {
            if j + i >= s.count {
                tmp += str[j...].joined()
                break
            }
            
            let base = str[j..<(j + i)].joined()
            var count = 0
            
            while true {
                if j + i > s.count { break }
                if str[j..<(j + i)].joined() == base {
                    count += 1
                } else {
                    break
                }
                j += i
            }
            tmp += count > 1 ? String(count) + base : base
        }
        
        answer = min(answer, tmp.count)
    }
    
    return answer
}