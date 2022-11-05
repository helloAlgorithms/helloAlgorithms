def solution(input_list : list, input_list_len : int) -> list:
    return [sum(input_list) // input_list_len, input_list[2]]

def runtime() -> None:
    inputs = []
    for i in range(5):
        inputs.append(int(input()))
    ans = solution(sorted(inputs), 5)
    print(ans[0])
    print(ans[1])

if __name__ == "__main__":
    runtime()