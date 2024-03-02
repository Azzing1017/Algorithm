def solution(n, computers):
    parents = [i for i in range(n)]

    def find(a):
        if parents[a] == a:
            return a
        parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        aP = find(a)
        bP = find(b)

        if aP < bP:
            parents[bP] = aP
        else:
            parents[aP] = bP

    for row in range(n):
        for col in range(n):
            if row == col:
                continue

            if computers[row][col]:
                union(row, col)

    ans = set()
    for i in range(n):
        ans.add(find(parents[i]))
    return len(ans)