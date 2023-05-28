func solution(_ s:String) -> String {
    var camel = s.split(separator: " ", omittingEmptySubsequences: false).map { String($0) }
    return camel.map {
        if $0 == "" { return "" }
        var str = Array($0).map { String($0).lowercased() }
        str[0] = String(str[0].uppercased())
        return str.joined()
    }.joined(separator: " ")
}
