import Foundation

func solution(_ picks:[Int], _ minerals:[String]) -> Int {
    var answer = 0
    var pick = picks
    var fetigue = Array(repeating: 0, count: minerals.count / 5 + (minerals.count % 5 > 0 ? 1 : 0))
    var idx = 0

    while idx < minerals.count {
        for i in 0..<5 {
            guard idx + i < minerals.count else { break }
            switch minerals[idx + i] {
            case "diamond":
                fetigue[idx / 5] += 100
            case "iron":
                fetigue[idx / 5] += 10
            case "stone":
                fetigue[idx / 5] += 1
            default:
                break
            }
        }
        idx += 5
    }

    let pickCount = pick.reduce(0, +)
    if pickCount < fetigue.count {
        fetigue = Array(fetigue[0..<pickCount])
    }

    for total in fetigue.sorted { $0 > $1 } {
        if pick[0] > 0 {
            answer += total / 100 + total % 100 / 10 + total % 10
            pick[0] -= 1
            continue
        }
        if pick[1] > 0 {
            answer += (total / 100) * 5 + total % 100 / 10 + total % 10
            pick[1] -= 1
            continue
        }
        if pick[2] > 0 {
            answer += (total / 100) * 25 + (total % 100 / 10) * 5 + total % 10
            pick[2] -= 1
            continue
        }
    }

    return answer
}
