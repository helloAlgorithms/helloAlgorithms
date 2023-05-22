func solution(_ x:Int) -> Bool {
    return x % String(x).map { Int(String($0))! }.reduce(0, +) == 0
}
