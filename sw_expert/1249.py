import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list((input().strip())) for _ in range(N)]

    

    def bfs():

        q = deque()
        q.append((0,0,0))
        
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        INF = 10**9
        dist = [[INF]*N for _ in range(N)]
        dist[0][0] = 0

        while q:

            r,c,t = q.popleft()


            for i in range(4):

                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0<= nr < N and 0<= nc < N:
                    new_cost = t + int(board[nr][nc])
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        q.append((nr,nc,new_cost))

        return dist[N-1][N-1]
    ans = bfs()
    print(f"#{tc} {ans}")
                

                

