import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var answer = 1
    var prior = priorities
    var location = location
    while prior.count > 0 {
        if prior[0] < prior.max()! {
            prior.append(prior[0])
        } else {
            if location == 0 { return answer }
            answer += 1
        }
        prior.removeFirst()
        location -= 1
        if location < 0 {
            location = prior.count - 1
        }
    }
    return answer
}