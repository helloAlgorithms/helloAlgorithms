func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    return arr1.enumerated().map { (i, a) in
        return a.enumerated().map { (j, b) in
            return b + arr2[i][j]
        }
    }
}
