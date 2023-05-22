func solution(_ n:Int, _ m:Int) -> [Int] {
    func gcd(_ n: Int, _ m: Int) -> Int {
        return m > 0 ? gcd(m, n % m) : n
    }
    var g = gcd(max(n, m), min(n, m))
    return [g, n * m / g]
}
