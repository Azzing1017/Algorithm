H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [[0]*W for _ in range(H)]

for x in range(H+X):
    for y in range(W+Y):
        if x < X and y < W:
            A[x][y] = B[x][y]
        elif X <= x < H and y < Y:
            A[x][y] = B[x][y]
        elif X <= x < H and Y <= y < W:
            A[x][y] = B[x][y] - A[x - X][y - Y]
        elif X <= x < H and W <= y < W+Y:
            A[x - X][y - Y] = B[x][y]
        else:
            A[x - X][y - Y] = B[x][y]

print('\n'.join([' '.join(map(str, row)) for row in A]))
