import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var reporter: [String: Set<String>] = [:]
    var reported: [String: Int] = [:]

    for rep in report {
        let fromto = rep.split(separator: " ").map {String($0)}
        reporter[fromto[0], default: Set<String>()].insert(fromto[1])
    }
    for reports in reporter {
        for to in reports.value {
            reported[to, default: 0] += 1
        }
    }

    return id_list.map {
        var mail = 0
        reporter[$0]?.forEach {
            if reported[$0]! >= k {
                mail += 1
            }
        }
        return mail
    }
}
