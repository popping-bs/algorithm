import sys
from collections import deque

sys.stdin = open('input.txt','r')

input = sys.stdin.readline

N,M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]


#'.', '#', 'O', 'R', 'B' 
dr = (1,-1,0,0)
dc = (0,0,1,-1)

pos = {}
for i , row in enumerate(board):
    for j, v in enumerate(row):
        if v in ('R', 'B'):
            pos[v] = (i,j)
            board[i][j] = '.'
rr, rc = pos['R']
br, bc = pos['B']


def move(r,c,d):
    cnt = 0
    while True:
        nr,nc = r + dr[d], c+ dc[d]
        if board[nr][nc] == "#":
            break
        r, c = nr, nc
        cnt += 1
        if board[r][c] == 'O':
            break
    return r,c,cnt

def bfs(rr,rc,br,bc):

    q = deque()
    q.append((rr,rc,br,bc,0))
    visited = set()
    visited.add((rr,rc,br,bc))
    
    while q:

        rr,rc,br,bc,depth = q.popleft()

        if depth >= 10:
            continue

        for d in range(4):

            nrr,nrc,rmove = move(rr,rc,d)
            nbr,nbc,bmove = move(br,bc,d)


            if board[nbr][nbc] == 'O':
                continue

            if board[nrr][nrc] == 'O':
                return depth +1
            
            if (nrr,nrc) == (nbr,nbc):
                if rmove> bmove:
                    nrr -= dr[d]; nrc -= dc[d]
                else:
                    nbr -= dr[d]; nbc -= dc[d]

            state = (nrr,nrc,nbr,nbc)
            if state not in visited:
                visited.add(state)
                q.append((nrr,nrc,nbr,nbc,depth+1))
    return -1
                

print(bfs(rr,rc,br,bc))