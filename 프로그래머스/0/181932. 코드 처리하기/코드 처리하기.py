def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] != '1':
            if mode == 0:
                if idx % 2 == 0:
                    answer += code[idx]
            elif mode == 1:
                if idx % 2 == 1:
                    answer += code[idx]
        elif code[idx] == '1':
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
    if answer == '':
        answer = 'EMPTY'
    return answer