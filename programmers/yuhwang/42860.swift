import Foundation

func solution(_ name:String) -> Int {
    var answer = 0

    let name = Array(name).map { String($0) }
    var word = Array(repeating: "A", count: name.count)
    if name == word { return 0 }

    var idx = 0

    while word.joined() != name {
        if word[idx] == name[idx] {
            var l = 0
            var r = 0

            var i = idx
            while word[i] == name[i] {
                i -= 1
                if i < 0 { i = word.count - 1 }
                l += 1
            }

            i = idx
            while word[i] == name[i] {
                i += 1
                if i >= word.count { i = 0 }
                r += 1
            }

            idx = i
            answer += r < l ? r : l
        }

        var diff: Int = Int(Character(name[idx]).asciiValue! - Character(word[idx]).asciiValue!)
        answer += diff <= 13 ? diff : 26 - diff
        word[idx] = name[idx]
    }
    return answer
}
