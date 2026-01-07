import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

SHIFT = 500
SIZE  = 2005

board = [[0] * SIZE for _ in range(SIZE)]
visited = [[False] * SIZE for _ in range(SIZE)]
dx = (-1,1,0,0)
dy = (0,0,-1,1)

def conv(x,y):
    X = (x+SHIFT) * 2
    Y = (y+SHIFT) * 2
    return X,Y

ox,oy = conv(0,0)
board[oy][ox] = 1

#사각형 테두리 그림
for _ in range(N):
    x1,y1,x2,y2 = map(int, input().split())

    if x1 > x2 : x1, x2 = x2 , x1
    if y1 > y2 : y1, y2 = y2 , y1

    X1,Y1 = conv(x1,y1)
    X2,Y2 = conv(x2,y2)

    for x in range(X1,X2+1):
        board[Y1][x] = 1
        board[Y2][x] = 1

    for y in range(Y1,Y2+1):
        board[y][X1] = 1
        board[y][X2] = 1

def bfs(sx,sy):

    q = deque()
    q.append((sx,sy))
    visited[sy][sx] = True

    while q:

        x,y = q.popleft()

        for dir in range(4):

            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0<= nx < SIZE and 0<= ny <SIZE:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx,ny))


components = 0

for y in range(SIZE):
    for x in range(SIZE):
        if board[y][x] ==1 and not visited[y][x]:
            components+=1
            bfs(x,y)

print(components-1)