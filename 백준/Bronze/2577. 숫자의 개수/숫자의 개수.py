A = int(input())
B = int(input())
C = int(input())

list_input = list(str(A*B*C))

list_count = [0] * 10

for i in list_input:
    list_count[int(i)] = list_count[int(i)] + 1

for i in list_count:
    print(i)