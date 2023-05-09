import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var zerocount = lottos.filter {$0 == 0}.count
    var samecount = lottos.filter { win_nums.contains($0) }.count
    return [7 - samecount - zerocount, 7 - (samecount == 0 ? 1 : samecount)]
}
