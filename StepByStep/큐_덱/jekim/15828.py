import sys
input = sys.stdin.readline

class PacketBuffer:
    def __init__(self, size):
        self.size = 0
        self.max_size = size
        self.buffer = []

    def push(self, data):
        if self.size == self.max_size:
            return False
        self.buffer.append(data)
        self.size += 1
        return True
    
    def pop(self):
        if self.size == 0:
            return False
        self.buffer.pop(0)
        self.size -= 1
        return True
    
def solution(line, N):
    buffer = PacketBuffer(N)
    for packet in line:
        if packet == 0:
            buffer.pop()
        else:
            buffer.push(packet)
    return " ".join(map(str, buffer.buffer))

def runtime () -> None :
    N = int(input().rstrip())
    line = []
    while True:
        packet = int(input().rstrip())
        if packet == -1:
            break
        line.append(packet)
    print(solution(line, N))

if __name__ == "__main__":
    runtime()