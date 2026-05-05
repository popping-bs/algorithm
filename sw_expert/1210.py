import sys
from collections import deque
sys.stdin = open('input.txt','r')

input = sys.stdin.readline


def solve(ladder):
    N = 100

    r = 99
    c = ladder[99].index(2)

    while r>0:
        if c > 0 and ladder[r][c-1] == 1:
            while c > 0 and ladder[r][c-1] ==1:
                c -= 1
        elif c < N-1 and ladder[r][c+1] == 1:
            while c < N-1 and ladder[r][c+1] ==1:
                c +=1

        r -= 1

    return c


for tc in range(1, 11):
    _ = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    ans = solve(ladder)
    print(f"#{tc} {ans}")


                