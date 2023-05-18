func solution(_ a:Int, _ b:Int) -> Int64 {
    let a: Int64 = Int64(a)
    let b: Int64 = Int64(b)
    return (a + b) * (abs(a - b) + 1) / 2
}
