import Foundation

func solution(_ m:String, _ musicinfos:[String]) -> String {
    var m = m
    m = m.replacingOccurrences(of: "C#", with: "c")
    m = m.replacingOccurrences(of: "D#", with: "d")
    m = m.replacingOccurrences(of: "F#", with: "f")
    m = m.replacingOccurrences(of: "G#", with: "g")
    m = m.replacingOccurrences(of: "A#", with: "a")
    
    let infos: [(playtime: Int, name: String, melody: String)] = musicinfos.map { info in
        var splited = info.split(separator: ",").map { String($0) }
        let start = splited[0].split(separator: ":").map { Int(String($0))! }
        let end = splited[1].split(separator: ":").map { Int(String($0))! }
        let playtime = (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])
        var melody = splited[3]
        melody = melody.replacingOccurrences(of: "C#", with: "c")
        melody = melody.replacingOccurrences(of: "D#", with: "d")
        melody = melody.replacingOccurrences(of: "F#", with: "f")
        melody = melody.replacingOccurrences(of: "G#", with: "g")
        melody = melody.replacingOccurrences(of: "A#", with: "a")
        var newmelody = ""
        for _ in 0..<(playtime / melody.count) {
            newmelody += melody
        }
        newmelody += melody[...melody.index(melody.startIndex, offsetBy: playtime % melody.count)]
        return (playtime, splited[2], newmelody)
    }.sorted { $0.playtime > $1.playtime }
    for info in infos {
        if info.melody.contains(m) {
            return info.name
        }
    }
    
    return "(None)"
}
