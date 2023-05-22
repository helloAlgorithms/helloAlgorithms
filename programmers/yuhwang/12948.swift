func solution(_ phone_number:String) -> String {
    return String(repeating: "*", count: phone_number.count - 4) + String(phone_number.suffix(4))
}
