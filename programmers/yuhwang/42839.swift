import Foundation

func solution(_ numbers:String) -> Int {
    func isprime(_ number: Int) -> Bool {
        if number < 2 { return false }
        var i = 2
        while i * i <= number {
            if number % i == 0 {
                return false
            }
            i += 1
        }
        return true
    }
    
    var nums: Set<Int> = Set<Int>()
    let numbers = Array(numbers).map { Int(String($0))! }
    var visited = Array(repeating: false, count: numbers.count)
    func recursive(_ num: Int, _ count: Int) {
        if count > numbers.count { return }
        if num > 0 {
            nums.insert(num)
        }
        for i in 0..<numbers.count {
            if visited[i] { continue }
            visited[i] = true
            recursive(num * 10 + numbers[i], count + 1)
            visited[i] = false
        }
    }
    recursive(0, 0)

    return nums.filter { isprime($0) }.count
}