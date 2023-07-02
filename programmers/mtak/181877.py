def solution(myString):
    return "".join(map(lambda x: chr(ord(x) - 32) if not 65 <= ord(x) <= 96 else x,myString))
