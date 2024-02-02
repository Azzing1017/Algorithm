def go(A):
    sum_all = 0
    for i in A:
        sum_all += i*i
    return sum_all % 10

list_input = list(map(int, input().split()))

print(go(list_input))