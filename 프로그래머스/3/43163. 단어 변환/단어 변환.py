from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    l = len(target)
    que = deque([])
    que.append([begin, 0])
    while que:
        word_pre, cnt = que.pop()
        for word in words:
            c = 0
            for i in range(l):
                if word_pre[i] != word[i]:
                    c += 1
                if c > 1:
                    break
            if c == 1:
                if word == target:
                    return cnt+1
                que.append([word, cnt+1])
    if not que:
        return 0