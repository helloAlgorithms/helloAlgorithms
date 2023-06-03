func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    var total = ""
    var answer = ""
    var p = p
    if p == m { p = 0 }
    
    for i in 0...(t * m) {
        total += String(i, radix: n).uppercased()
    }
    
    for (i, c) in total.enumerated() {
        if (i + 1) % m == p {
            answer += String(c)
        }
        if answer.count == t { break }
    }
    
    return answer
}