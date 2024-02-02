N = int(input())
n = 50
list_input = [[] for _ in range(50)]

for _ in range(N):
    word = input()
    index = len(word)-1
    if word not in list_input[index]:
        list_input[index].append(word)

for i in list_input:
    i.sort()
    for j in i:
        print(j)