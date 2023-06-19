import Foundation

func solution(_ w: Int, _ h: Int) -> Int64 {
    let x = max(w, h)
    let y = min(w, h)
    
    func uclid(_ a: Int, _ b: Int) -> Int {
        return a % b == 0 ? b : uclid(b, a % b)
    }
    
    let gcd = uclid(x, y)
    let a = x / gcd
    let b = y / gcd
    
    return (Int64(x) * Int64(y)) - ((Int64(a) + Int64(b) - 1) * (Int64(y) / Int64(b)))
}