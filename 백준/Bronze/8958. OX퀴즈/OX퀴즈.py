import sys
T = int(input())
list_input = [list(map(str, list(input()))) for _ in range(T)]
list_answer = []

for i in list_input:
    pro = ''
    sum_now = 1
    sum_score = 0
    for j in i:
        if j == 'O':
            sum_score += sum_now
            pro = 'O'
            sum_now += 1
        elif j == 'X':
            pro = 'X'
            sum_now = 1
    list_answer.append(sum_score)

sys.stdout.write('\n'.join(map(str, list_answer))+'\n')