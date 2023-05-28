func solution(_ s:String) -> String {
    let s = s.split(separator: " ").map { Int(String($0))! }.sorted()
    return "\(s[0]) \(s.last!)"
}
