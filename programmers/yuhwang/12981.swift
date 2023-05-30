import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var s = Set<String>()
    for (idx, word) in words.enumerated() {
        if idx != 0 && word.first! != words[idx - 1].last! || s.contains(word) {
            return [(idx + 1) % n == 0 ? n : idx % n + 1, idx / n + 1]
        }
        s.insert(word)
    }
    return [0, 0]
}
