func solution(_ s:String) -> String {
    return s.split(separator: " ", omittingEmptySubsequences: false).map {
        return Array(String($0)).enumerated().map { (i, c) in
            if i % 2 == 0 {
                return String(c).uppercased()
            } else {
                return String(c).lowercased()
            }
        }.joined()
    }.joined(separator: " ")
}
