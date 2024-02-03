N = int(input())
li = [[i] + [int(x) if x.isdigit() else x for x in input().split()] for i in range(N)]

li.sort(key=lambda x:(x[1], x[0]))

for i in li:
    print(f'{i[1]} {i[2]}')