def solution(name):
    answer = 0
    if set(name) == {'A'}:
        return 0
    l = len(name)
    nona = sum(1 for char in name if char != 'A')
    idx = [n for n in range(l)]
    ans = []
    for i in range(1, l):
        rl = idx[0:1] + idx[1:i+1] + idx[:i][::-1] + idx[-1:i-l:-1]
        lr = idx[0:1] + idx[-1:-i-1:-1] + idx[-1:-i:-1][::-1] + idx[:-i+l]
        for li in [rl, lr]:
            cnt = 0
            chk = 0
            tmp = [s for s in name]
            for i in li:
                cnt += 1
                if tmp[i] != 'A':
                    cnt += min(ord(tmp[i])-65, 91-ord(tmp[i]))
                    tmp[i] = 'A'
                    chk += 1
                if chk == nona:
                    break
            ans.append(cnt-1)
    answer = min(ans) 
    return answer
                