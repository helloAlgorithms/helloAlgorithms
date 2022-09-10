import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.Container = []

    def get_size(self) -> int: return len(self.Container)
    
    def insert(self, number : int, logger : list) -> int:
        self.Container.append(number)
        logger.append("+")
        return 0
    
    def pop(self, logger : list) -> int:
        if len(self.Container) != 0:
            self.Container.pop(-1)
            logger.append("-")
            return 0
        else:
            return -1
    
    def peek(self) -> int:
        if len(self.Container) != 0: return self.Container[-1]

def solution(input_list : list, input_length : int) -> list:
    answer = []
    number_list = range(1, input_length + 1)
    mystack = stack()
    i = 0
    cur = 1
    for i in range(input_length):
        while cur <= input_list[i]:
            mystack.insert(cur, answer)
            cur += 1
        if mystack.peek() == input_list[i]:
            mystack.pop(answer)
        else:
            return ["NO"]
    return answer

def print_list_by_line(lst : list) -> None:
    for i in lst: print(i)

def runtime() -> None:
    input_length = int(input().rstrip())
    input_list = []
    for _ in range(input_length): input_list.append(int(input().rstrip()))
    print_list_by_line(solution(input_list, input_length))

if __name__ == "__main__": runtime()