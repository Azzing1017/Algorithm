def solution(num_list):
    answer = []
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        num_list.append(a-b)
    else:
        num_list.append(a*2)
    answer = num_list
    return answer