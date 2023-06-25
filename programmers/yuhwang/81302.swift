import Foundation

func solution(_ places:[[String]]) -> [Int] {
    return places.map { place in
        var room = place.map {
            $0.map { String($0) }
        }
        for x in 0..<5 {
            for y in 0..<5 {
                if room[x][y] == "P" {
                    if x - 1 >= 0 && room[x - 1][y] == "P" { return 0 }
                    if x + 1 < 5 && room[x + 1][y] == "P" { return 0 }
                    if y - 1 >= 0 && room[x][y - 1] == "P" { return 0 }
                    if y + 1 < 5 && room[x][y + 1] == "P" { return 0 }
                    
                    if (x - 1 >= 0 && y - 1 >= 0) && room[x - 1][y - 1] == "P" && (room[x - 1][y] == "O" || room[x][y - 1] == "O") { return 0 }
                    if (x - 1 >= 0 && y + 1 < 5) && room[x - 1][y + 1] == "P" && (room[x - 1][y] == "O" || room[x][y + 1] == "O") { return 0 }
                    if (x + 1 < 5 && y - 1 >= 0) && room[x + 1][y - 1] == "P" && (room[x + 1][y] == "O" || room[x][y - 1] == "O") { return 0 }
                    if (x + 1 < 5 && y + 1 < 5) && room[x + 1][y + 1] == "P" && (room[x + 1][y] == "O" || room[x][y + 1] == "O") { return 0 }
                    
                    if x - 2 >= 0 && room[x - 2][y] == "P" && room[x - 1][y] == "O" { return 0 }
                    if x + 2 < 5 && room[x + 2][y] == "P" && room[x + 1][y] == "O" { return 0 }
                    if y - 2 >= 0 && room[x][y - 2] == "P" && room[x][y - 1] == "O" { return 0 }
                    if y + 2 < 5 && room[x][y + 2] == "P" && room[x][y + 1] == "O" { return 0 }
                }
            }
        }
        return 1
    }
}