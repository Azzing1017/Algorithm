cnt = 0

def dfs(index, total, numbers, target):
    global cnt
    if index == len(numbers):
        if total == target:
            cnt += 1
        return
    else:
        dfs(index + 1, total + numbers[index], numbers, target)
        dfs(index + 1, total - numbers[index], numbers, target)

def solution(numbers, target):
    global cnt
    dfs(1, numbers[0], numbers, target)
    dfs(1, -numbers[0], numbers, target)
    return cnt