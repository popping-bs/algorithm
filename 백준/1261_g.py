import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M , N = map(int, input().split())
board = []
INF = 10**9
dist = [[INF]* M for _ in range(N)]

for _ in range(N):
    s = input().strip()
    board.append(list(map(int,s)))


dr = (1,-1,0,0)
dc = (0,0,1,-1)


def bfs():


    q = deque()
    q.append((0,0))
    dist[0][0] = 0

    while q:

        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0<= nr < N and 0<= nc < M):
                continue

            cost = board[nr][nc]
            nd = dist[r][c] + cost

            if nd < dist[nr][nc]:
                dist[nr][nc] = nd

                if cost == 0:
                    q.appendleft((nr,nc))
                else:
                    q.append((nr,nc))

    return dist[N-1][M-1]

print(bfs())