def solution(input_str : str, input_str_len : int) -> int:
    s = set()
    string = ""
    for i in range(input_str_len):
        for j in range(i, input_str_len):
            string += input_str[j]
            s.add(string)
        string = ""
    return len(s)

def runtime():
    input_str = input()
    print(solution(input_str, len(input_str)))

runtime()