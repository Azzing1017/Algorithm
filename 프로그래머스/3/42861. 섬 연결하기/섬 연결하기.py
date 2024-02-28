def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    root = [i for i in range(n)]
    answer = 0

    def find(x):
        if root[x] == x:
            return x
        else:
            root[x] = find(root[x])
            return root[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        root[root_y] = root_x

    for cost in costs:
        x, y, z = cost
        if find(x) != find(y):
            union(x, y)
            answer += z

    return answer
