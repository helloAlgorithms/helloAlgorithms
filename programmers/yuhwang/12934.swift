import Foundation

func solution(_ n:Int64) -> Int64 {
    return sqrt(Double(n)) == Double(Int64(sqrt(Double(n)))) ? Int64(sqrt(Double(n)) + 1) * Int64(sqrt(Double(n)) + 1) : -1
}
