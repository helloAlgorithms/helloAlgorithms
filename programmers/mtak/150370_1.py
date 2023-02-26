class Date:
    def __init__(self, date):
        tmp = date.split('.')
        self.amount = (int(tmp[0]) * 12 + int(tmp[1])) * 28 + int(tmp[2])
    def __add__(self,t):
        self.amount += t * 28
    
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
        if date.amount <= today.amount:
            answer.append(idx + 1)
    return answer
