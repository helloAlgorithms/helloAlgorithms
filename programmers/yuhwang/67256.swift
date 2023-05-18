import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var answer = ""
    var l: (Int, Int) = (0, 3)
    var r: (Int, Int) = (2, 3)
    for i in numbers {
        switch i {
        case 1, 4, 7:
            answer += "L"
            l = (0, i / 3)
        case 3, 6, 9:
            answer += "R"
            r = (2, i / 3 - 1)
        case 2, 5, 8:
            let lgap = abs(l.0 - 1) + abs(l.1 - i / 3)
            let rgap = abs(r.0 - 1) + abs(r.1 - i / 3)
            if lgap > rgap {
                answer += "R"
                r = (1, i / 3)
            } else if lgap < rgap {
                answer += "L"
                l = (1, i / 3)
            } else {
                if hand == "left" {
                    answer += "L"
                    l = (1, i / 3)
                } else {
                    answer += "R"
                    r = (1, i / 3)
                }
            }
        default:
            let lgap = abs(l.0 - 1) + abs(l.1 - 3)
            let rgap = abs(r.0 - 1) + abs(r.1 - 3)
            if lgap > rgap {
                answer += "R"
                r = (1, 3)
            } else if lgap < rgap {
                answer += "L"
                l = (1, 3)
            } else {
                if hand == "left" {
                    answer += "L"
                    l = (1, 3)
                } else {
                    answer += "R"
                    r = (1, 3)
                }
            }
        }
    }
    return answer
}
