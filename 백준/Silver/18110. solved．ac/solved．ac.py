n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()

def round2(num):
    return int(num) + (1 if (num - int(num)) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    num = round2(n*0.15)
    li = li[num:n-num]

    print(round2(sum(li)/(n-2*num)))