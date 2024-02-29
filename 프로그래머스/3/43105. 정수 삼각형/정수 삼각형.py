def solution(triangle):
    answer = 0
    l = len(triangle)
    for i in range(1, l):
        triangle[i][0] += triangle[i-1][0]
        for j in range(1, i):
            triangle[i][j] = max(triangle[i][j]+triangle[i-1][j-1], triangle[i][j]+triangle[i-1][j])
        triangle[i][i] += triangle[i-1][i-1]
    answer = max(triangle[l-1])
            
    return answer