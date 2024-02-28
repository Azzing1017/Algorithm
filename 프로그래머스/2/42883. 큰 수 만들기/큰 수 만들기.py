from collections import deque

def solution(number, k):
    answer = ''
    number = deque(list(map(int, number)))
    ans = []
    ans.append(number.popleft())
    while number and k!=0:
        x = number.popleft()
        while ans and k!=0:
            if x > ans[-1]:
                ans.pop()
                k -= 1
            else:
                break
        ans.append(x)
    if k == 0:
        ans += number
    else:
        for _ in range(k):
            ans.pop()
    answer = ''.join(map(str, ans))
    return answer