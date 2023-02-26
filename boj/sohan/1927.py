import sys

class heap:
    def __init__(self):
        self.arr = [0] * (10**5 + 2)
        self.size = 0

    def insert(self, data):
        self.size = self.size + 1
        i = self.size
    
        while i != 1 and data < self.arr[i // 2]:
            self.arr[i] = self.arr[i // 2]
            i = i // 2
        
        self.arr[i] = data
    
    def delete(self):
        if self.size == 0:
            return 0
        ret = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.size = self.size - 1
        parent = 1
    
        while True:
            child = parent * 2
            if child + 1 <= self.size and self.arr[child] > self.arr[child + 1]:
                child += 1
    
            if child > self.size or self.arr[child] > self.arr[parent]:
                break
    
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            parent = child
    
        return ret

N = int(input())
ops = [int(sys.stdin.readline()) for _ in range(N)]
ans = ""
h = heap()

for op in ops:
    if op > 0:
        h.insert(op)
    else:
        print(h.delete())
