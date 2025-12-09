#직사각형으로 나누기


import sys

sys.stdin = open('input.txt', 'r')

n , m = map(int,sys.stdin.readline().split())

square_size = [[0] * m for _ in range(n)]

for r in range(n):
    raw = list(map(int, sys.stdin.readline().strip()))
    square_size[r] = raw
 
ps = [[0] * (m+1) for _ in range(n+1)]

max_val= 0

for i in range(1,n+1):
    for j in range(1, m+1):
        ps[i][j] = (
            ps[i-1][j]
            + ps[i][j-1]
            -ps[i-1][j-1]
            +square_size[i-1][j-1]
        )

def rect_sum(r1,c1,r2,c2):
    return (
        ps[r2+1][c2+1]
        -ps[r1][c2+1]
        -ps[r2+1][c1]
        +ps[r1][c1]
    )

for c1 in range(0, m-2):
    for c2 in range(c1+1, m-1):
        s1 = rect_sum(0, 0,   n-1, c1)
        s2 = rect_sum(0, c1+1, n-1, c2)
        s3 = rect_sum(0, c2+1, n-1, m-1)
        prod = s1 * s2 * s3
        if prod > max_val:
            max_val = prod

# ▷ 케이스 2: 가로로 3등분
for r1 in range(0, n-2):
    for r2 in range(r1+1, n-1):
        s1 = rect_sum(0,     0, r1,   m-1)
        s2 = rect_sum(r1+1,  0, r2,   m-1)
        s3 = rect_sum(r2+1,  0, n-1,  m-1)
        prod = s1 * s2 * s3
        if prod > max_val:
            max_val = prod

for c in range(0, m-1):
    for r in range(0, n-1):
        s1 = rect_sum(0,0,n-1,c)
        s2 = rect_sum(0,c+1, r , m-1)
        s3 = rect_sum(r+1,c+1,n-1,m-1)

        prod = s1* s2 * s3
        if prod > max_val:
            max_val = prod

for c in range(0, m-1):
    for r in range(0, n-1):
        s1 = rect_sum(0, c+1, n-1, m-1)
        s2 = rect_sum(0, 0, r, c)
        s3 = rect_sum(r+1,0, n-1, c)
        
        prod = s1 * s2 * s3
        if prod > max_val:
            max_val = prod

for r in range(0, n-1):
    for c in range(0, m-1):
        s1 = rect_sum(0,0, r, m-1)
        s2 = rect_sum(r+1,0, n-1, c)
        s3 = rect_sum(r+1, c+1, n-1, m-1)

        prod = s1 * s2 * s3
        if prod > max_val:
            max_val = prod

for r in range(0, n-1):
    for c in range(0, m-1):
        s1 = rect_sum(r+1,0, n-1,m-1)
        s2 = rect_sum(0,0, r, c)
        s3 = rect_sum(0, c+1, r, m-1)

        prod = s1 * s2 * s3
        if prod > max_val:
            max_val = prod

print(max_val)