def solution(num_list):
    answer = 0
    num_odd = ''
    num_even = ''
    for i in num_list:
        if i % 2 == 1:
            num_odd += str(i)
        else:
            num_even += str(i)
    answer = int(num_odd) + int(num_even)
    return answer