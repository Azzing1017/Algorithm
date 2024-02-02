N, K = map(int, input().split())
li = [n for n in range(1, N+1)]
li_a = []

len_li = len(li)
index = 0
while len_li > 0:
    index = index + K - 1
    while index >= len_li:
        index = index - len_li
    li_a.append(li[index])
    li.pop(index)
    len_li -= 1    

print('<'+ ', '.join(map(str, li_a))+'>')