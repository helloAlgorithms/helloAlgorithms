def solution(record):
    answer = []
    
    table = {}
    commands = []
    for r in record:
        tmp = r.split()
        com = tmp[0]
        uid = tmp[1]
        if com in ['Enter', 'Change']:
            name = tmp[2]
            table[uid] = name
            if com == 'Enter':
                commands.append(['E', uid])
        else:
            commands.append(['L', uid])
    for com in commands:
        com, uid = com
        name = table[uid]
        if com == 'E':
            name += '님이 들어왔습니다.'
        else:
            name += '님이 나갔습니다.'
        answer.append(name)
        
            
    return answer
