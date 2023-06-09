import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    let build = Array(skill)
    return skill_trees.filter {
        let skills = $0.filter { skill.contains($0) }
        for (i, c) in skills.enumerated() {
            if c != build[i] { return false }
        }
        return true
    }.count
}