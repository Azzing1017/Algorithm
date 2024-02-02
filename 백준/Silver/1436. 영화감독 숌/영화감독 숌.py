import sys
input = sys.stdin.readline

N = int(input())
list_select = [0] * 4

list_answer = []

def go(index):
    if index == 4:
        for i in range(5):
            list_select.insert(i, 666)
            num = int(''.join(map(str, list_select)))
            if num not in list_answer:
                list_answer.append(num)
            list_select.remove(666)
        return
    else:
        for i in range(10):
            list_select[index] = i
            go(index+1)

go(0)
list_answer.sort()

sys.stdout.write(str(list_answer[N-1]))