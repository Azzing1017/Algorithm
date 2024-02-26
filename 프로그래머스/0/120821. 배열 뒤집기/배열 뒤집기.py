def solution(num_list):
    answer = []
    for i in range(0, len(num_list)//2):
        num_list[i], num_list[-1-i] = num_list[-1-i], num_list[i]
    answer = num_list
    return answer