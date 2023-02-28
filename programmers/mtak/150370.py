class Date:
    def __init__(self, date):
        tmp = date.split('.')
        self.year = int(tmp[0])
        self.month = int(tmp[1])
        self.day = int(tmp[2])
    def __add__(self,t):
        self.month += t
        while self.month > 12:
            self.year += self.month//12
            self.month = self.month%12
        if self.day - 1 <= 0:
            self.day = 28
            if self.month - 1 <= 0:
                self.year -= 1
                self.month += 12
            self.month -= 1
        else:
            self.day -= 1
    def __gt__(self, other):
        print(self, other)
        if self.year > other.year:
            return True
        if self.year == other.year and self.month > other.month:
            return True
        if self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        return False
    def __str__(self):
        return str(self.year) + str(self.month) + str(self.day)
    
def solution(today, terms, privacies):
    answer = []
    term = {}
    today = Date(today)
    for val in terms:
        k, v = val.split()
        term[k] = int(v)
    for idx, val in enumerate(privacies):
        date, t = val.split()
        date = Date(date)
        date + term[t]
        if today > date:
            answer.append(idx + 1)
    return answer
