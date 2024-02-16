A = int(input())
B = int(input())
C = int(input())
if (B < A < C) or (C < A < B):
    print(A)
elif (A < B < C) or (C < B < A):
    print(B)
elif (B < C < A) or (A < C < B):
    print(C)
