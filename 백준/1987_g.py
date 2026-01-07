import sys


sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

R, C = map(int, input().split())

visited = [[False]*C for _ in range(R)]
board = [list(input().rstrip()) for _ in range(R)]
used = [board[0][0]]
max_len = 0

dx = (1,-1,0,0)
dy = (0,0,1,-1)



def dfs(r,c,l):
    global max_len
    max_len = max(max_len, l)
    for i in range(4):

        nr = r + dx[i]
        nc = c + dy[i]

        if nr >= 0 and nr < R and nc>=0 and nc < C:
            if not visited[nr][nc] and board[nr][nc] not in used:
                used.append(board[nr][nc])
                visited[nr][nc] = True
                dfs(nr,nc,l+1)
                used.remove(board[nr][nc])
                visited[nr][nc] = False

visited[0][0] = True
dfs(0,0,1) 
print(max_len)