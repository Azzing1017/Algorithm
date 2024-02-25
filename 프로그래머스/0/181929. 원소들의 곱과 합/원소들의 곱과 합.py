def solution(num_list):
    answer = 0
    sum_all = 0
    mul_all = 1
    for i in num_list:
        sum_all += i
        mul_all *= i
    if mul_all < sum_all**2:
        answer = 1
    return answer