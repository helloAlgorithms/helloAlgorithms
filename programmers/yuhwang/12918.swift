func solution(_ s:String) -> Bool {
    for c in s {
        if !c.isNumber { return false }
    }
    return true
}
