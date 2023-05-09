import Foundation

func solution(_ name:String) -> Int {
    var vertical = 0
    let notA = name.filter { $0 != "A" }.count
    if notA == 0 { return 0 }
    for c in name {
        if c == "A" { continue }
        let gap: Int = Int(c.asciiValue! - Character("A").asciiValue!)
        vertical += gap <= 13 ? gap : 26 - gap
    }
    if !name.contains("A") { return vertical + name.count - 1 }

    var n = Array(name).map {String($0)}
    var horizon = n.count - 1
    var idx = 0
    var move = 0
    var c = notA
    if n[idx] == "A" {
        idx += 1
        move += 1
    }
    while idx < n.count && c > 0 {
        if n[idx] != "A" {
            c -= 1
            n[idx] = "A"
        } else {
            var tmp = n
            var nota = c
            var i = idx - 1 < 0 ? n.count - 1 : idx - 1
            var m = move
            while nota > 0 {
                i -= 1
                if i < 0 { i = n.count - 1 }
                if tmp[i] != "A" {
                    tmp[i] = "A"
                    nota -= 1
                }
                if nota > 0 { m += 1 }
            }
            horizon = horizon > m ? m : horizon
        }
        if c == 0 {
            horizon = horizon > move ? move : horizon
            break
        }
        move += 1
        idx += 1
    }

    n = Array(name).map { String($0) }
    idx = n.count - 1
    move = 1
    c = notA
    if n[0] != "A" {
        c -= 1
        n[0] = "A"
    }
    if n[idx] == "A" {
        idx -= 1
        move += 1
    }
    while idx > 0 {
        if n[idx] != "A" {
            c -= 1
            n[idx] = "A"
        } else {
            var tmp = n
            var nota = c
            var i = idx + 1 >= n.count ? 0 : idx + 1
            var m = move - 1
            while nota > 0 {
                i += 1
                if i >= n.count { i = 0 }
                if tmp[i] != "A" {
                    tmp[i] = "A"
                    nota -= 1
                }
                m += 1
            }
            horizon = horizon > m ? m : horizon
        }
        if c == 0 {
            horizon = horizon > move ? move : horizon
            break
        }
        move += 1
        idx -= 1
    }
    return vertical + horizon
}
