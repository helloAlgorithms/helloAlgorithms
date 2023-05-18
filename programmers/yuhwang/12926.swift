func solution(_ s:String, _ n:Int) -> String {
    let lowercase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz".map {String($0)}
    let uppercase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz".uppercased().map {String($0)}
    return s.map {
        if $0.isLowercase {
            return lowercase[(lowercase.firstIndex(of: String($0))! + n)]
        } else if $0.isUppercase {
            return uppercase[(uppercase.firstIndex(of: String($0))! + n)]
        }
        return String($0)
    }.joined()
}
