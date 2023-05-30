func solution(_ str1:String, _ str2:String) -> Int {
    var s1: [String] = []
    var s2: [String] = []
    let arr1 = str1.map { String($0) }
    let arr2 = str2.map { String($0) }
    for i in 0..<(arr1.count - 1) {
        if arr1[i].first!.isLetter && arr1[i + 1].first!.isLetter {
            s1.append((arr1[i] + arr1[i + 1]).lowercased())
        }
    }
    for i in 0..<(arr2.count - 1) {
        if arr2[i].first!.isLetter && arr2[i + 1].first!.isLetter {
            s2.append((arr2[i] + arr2[i + 1]).lowercased())
        }
    }
    if s1.count == 0 && s2.count == 0 { return 65536 }
    var union = 0
    var inter = 0
    var m: [String: Int] = [:]
    for word in s1 {
        m[word, default: 0] += 1
    }
    for word in s2 {
        if m[word] != nil && m[word]! > 0 {
            union += 1
            m[word]! -= 1
            if m[word]! == 0 {
                m.removeValue(forKey: word)
            }
        }
    }
    inter = s1.count + s2.count - union
    return Int((Double(union) / Double(inter)) * 65536)
}