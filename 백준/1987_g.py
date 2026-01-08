import sys


sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

R, C = map(int, input().split())

board = [input().strip() for _ in range(R)]
used = set([board[0][0]])
max_len = 0

dx = (1,-1,0,0)
dy = (0,0,1,-1)



def dfs(r,c,l):
    global max_len
    max_len = max(max_len, l)
    for i in range(4):

        nr = r + dx[i]
        nc = c + dy[i]

        if 0 <= nr < R and 0 <= nc < C:
            ch = board[nr][nc]
            if ch not in used:
                used.add(ch)
                dfs(nr,nc,l+1)
                used.remove(ch)

dfs(0,0,1) 
print(max_len)