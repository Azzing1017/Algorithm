def solution(answers):
    answer = []
    li1 = [1,2,3,4,5]
    li2 = [2,1,2,3,2,4,2,5]
    li3 = [3,3,1,1,2,2,4,4,5,5]
    cor1 = 0
    cor2 = 0
    cor3 = 0
    for i in range(len(answers)):
        if answers[i] == li1[i%5]:
            cor1 += 1
        if answers[i] == li2[i%8]:
            cor2 += 1
        if answers[i] == li3[i%10]:
            cor3 += 1
    cor_max = max(cor1, cor2, cor3)
    if cor1 == cor_max:
        answer.append(1)
    if cor2 == cor_max:
        answer.append(2)
    if cor3 == cor_max:
        answer.append(3)
    return answer