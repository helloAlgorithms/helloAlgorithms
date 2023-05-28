func solution(_ arr:[Int]) -> Int {
    var answer = arr[0]

    func valid() -> Bool {
        for i in 0..<arr.count {
            if answer % arr[i] != 0 { return false }
        }
        return true
    }

    while !valid() {
        answer += arr[0]
    }
    return answer
}
