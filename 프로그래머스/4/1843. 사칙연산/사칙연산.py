def solution(arr):
    answer = -1
    nums = []
    ops = []
    for i, v in enumerate(arr):
        nums.append(int(v)) if i%2==0 else ops.append(v)
    l = len(nums)
    INF_NEG = float('-inf')
    INF_POS = float('inf')
    dp_min = [[INF_POS for _ in range(l)] for _ in range(l)]
    dp_max = [[INF_NEG for _ in range(l)] for _ in range(l)]
    
    for scope in range(l):
        for start in range(l-scope):
            end = start + scope
            if scope == 0:
                dp_min[start][start] = dp_max[start][start] = nums[start]
            else:
                for i in range(start, end):
                    if ops[i] == '+':
                        dp_min[start][end] = min(dp_min[start][end], dp_min[start][i]+dp_min[i+1][end])
                        dp_max[start][end] = max(dp_max[start][end], dp_max[start][i]+dp_max[i+1][end])
                    elif ops[i] == '-':
                        dp_min[start][end] = min(dp_min[start][end], dp_min[start][i]-dp_max[i+1][end])
                        dp_max[start][end] = max(dp_max[start][end], dp_max[start][i]-dp_min[i+1][end])
    
    answer = dp_max[0][-1]
    return answer