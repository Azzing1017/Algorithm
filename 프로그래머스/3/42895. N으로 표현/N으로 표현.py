def solution(N, number):
    ans = {}
    op = ['+','-','*','/']
    for i in range(1, 9):
        tmp = set()
        tmp.add(int(str(N)*i))
        for j in range(1, i):
            for a in ans[i-j]:
                for b in ans[j]:
                    tmp.add(a+b)
                    tmp.add(a-b)
                    tmp.add(a*b)
                    if b!=0:
                        tmp.add(a/b)
        if number in tmp:
            return i
        else:
            ans[i] = tmp
    return -1