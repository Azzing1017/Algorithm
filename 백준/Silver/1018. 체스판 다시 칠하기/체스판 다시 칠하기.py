N, M = map(int, input().split())
list_input = [list(input()) for i in range(N)]
list_cr1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
list_cr2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

list_answer = []

for i in range(N-7):
    for j in range(M-7):
        count = 0 
        for a in range(8):
            for b in range(8):
                if list_input[i+a][j+b] != list_cr1[a][b]:
                    count += 1
        list_answer.append(count)
        count=0
        for a in range(8):
            for b in range(8):
                if list_input[i+a][j+b] != list_cr2[a][b]:
                    count += 1
        list_answer.append(count)

list_answer.sort()
print(list_answer[0])