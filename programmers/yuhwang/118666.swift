import Foundation

func solution(_ survey:[String], _ choices:[Int]) -> String {
    var answer = ""
    var point = ["R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0]
    for i in 0..<survey.count {
        switch choices[i] {
        case 1:
            point[String(survey[i].first!), default: 0] += 3
        case 2:
            point[String(survey[i].first!), default: 0] += 2
        case 3:
            point[String(survey[i].first!), default: 0] += 1
        case 5:
            point[String(survey[i].last!), default: 0] += 1
        case 6:
            point[String(survey[i].last!), default: 0] += 2
        case 7:
            point[String(survey[i].last!), default: 0] += 3
        default:
            break
        }
    }
    answer += point["R"]! >= point["T"]! ? "R" : "T"
    answer += point["C"]! >= point["F"]! ? "C" : "F"
    answer += point["J"]! >= point["M"]! ? "J" : "M"
    answer += point["A"]! >= point["N"]! ? "A" : "N"
    return answer
}
