func solution(_ files:[String]) -> [String] {
    return files.sorted {
        var str1 = $0
        var str2 = $1
        var head1 = ""
        var head2 = ""
        var num1 = 0
        var num2 = 0
        for c in str1 {
            if c.isNumber { break }
            head1 += String(c)
        }
        str1.removeFirst(head1.count)
        for c in str2 {
            if c.isNumber { break }
            head2 += String(c)
        }
        str2.removeFirst(head2.count)
        if head1.lowercased() != head2.lowercased() { return head1.lowercased() < head2.lowercased() }
        for c in str1 {
            if !c.isNumber { break }
            num1 *= 10
            num1 += Int(String(c))!
        }
        for c in str2 {
            if !c.isNumber { break }
            num2 *= 10
            num2 += Int(String(c))!
        }
        if num1 != num2 { return num1 < num2 }
        return false
    }
}