import Foundation

func solution(_ arr:[[Int]]) -> [Int] {
    var answer: [Int] = [0, 0]
    
    func recursive(_ x: Int, _ y: Int, _ r: Int) {
        let a = arr[x][y]
        var equal = true
        for i in 0..<r {
            for j in 0..<r {
                if arr[x + i][y + j] != a {
                    equal = false
                    break
                }
            }
            if !equal { break }
        }
        
        if equal {
            answer[a] += 1
            return
        }
        
        for i in 0..<2 {
            for j in 0..<2 {
                recursive(x + i * (r / 2), y + j * (r / 2), r / 2)
            }
        }
    }
    
    recursive(0, 0, arr.count)
    return answer
}