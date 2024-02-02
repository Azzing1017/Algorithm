import sys

N = int(input())
list_input = [list(map(int, input().split())) for _ in range(N)]

list_input.sort(key=lambda x: (x[1], x[0]))

for i in list_input:
    print(*i)