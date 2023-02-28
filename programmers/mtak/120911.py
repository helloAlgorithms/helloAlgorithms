def solution(my_string):
    ret = ''
    for i in my_string:
        if ord('A') <= ord(i) <= ord('Z'):
            ret += chr(ord(i) + 32)
            continue
        ret += i
    print(ret)
    return ''.join(sorted(ret))
