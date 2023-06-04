import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var answer = 0
    var totalWeight = 0
    var next = 0
    var bridge: [(time: Int, weight: Int)] = []
    bridge.append((answer, truck_weights[next]))
    totalWeight += truck_weights[next]
    next += 1
    
    while totalWeight > 0 {
        if bridge.first!.time + bridge_length <= answer {
            totalWeight -= bridge.first!.weight
            bridge.removeFirst()
        }
        if next < truck_weights.count && totalWeight + truck_weights[next] <= weight {
            totalWeight += truck_weights[next]
            bridge.append((answer, truck_weights[next]))
            next += 1
        }
        answer += 1
    }
    return answer
}