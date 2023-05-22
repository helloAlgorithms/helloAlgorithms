func solution(_ x:Int, _ n:Int) -> [Int64] {
    return (1...n).map { Int64($0) * Int64(x) }
}
