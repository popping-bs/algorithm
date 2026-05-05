import sys
from collections import deque

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
empties = []

for i , row in enumerate(board):
    for j , v in enumerate(row):
        if v == 0:
            empties.append((i,j))

dr = (1,-1,0,0)
dc = (0,0,1,-1)            

def bfs():
    tmp = [row[:] for row in board]

    q = deque()

    for i, row in enumerate(tmp):
        for j, v in enumerate(row):
            if v == 2:
                q.append((i,j))


    while q:

        r,c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0<= nr < N and 0<= nc < M:
                if tmp[nr][nc] == 0:
                    tmp[nr][nc] = 2
                    q.append((nr,nc))

    safe = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                safe+=1

    return safe
ans = 0 
def dfs(start, depth):
    global ans
    if depth == 3:
        ans = max(ans,bfs())
        return
    
    for i in range(start, len(empties)):
        r  = empties[i][0]
        c  = empties[i][1]
        board[r][c] = 1
        dfs(i+1, depth+1)
        board[r][c] = 0

dfs(0,0)
print(ans)

