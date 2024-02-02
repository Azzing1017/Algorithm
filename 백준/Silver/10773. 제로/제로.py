K = int(input())
list_input = []

for _ in range(K):
    num = int(input())
    if num == 0:
        list_input.pop()
    else:
        list_input.append(num)

print(sum(list_input))