import sys 


sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N,M,K = map(int, input().split())
board = list(input().rstrip() for _ in range(N))
word = input().rstrip()

L = len(word)

dp = [ [[-1]* L for _ in range(M)] for _ in range(N)]

dy = (-1,1,0,0)
dx = (0,0,-1,1)


def dfs(y,x,i):

    if board[y][x] != word[i]:
        return 0
    
    if i == L-1:
        return 1
    
    if dp[y][x][i] != -1:
        return dp[y][x][i]
 

    total = 0

    for dir in range(4):
        for step in range(1, K+1):
            ny = y + dy[dir] * step 
            nx = x + dx[dir] * step 
            if ny<0 or ny>= N or nx <0 or nx >=M:
                break
            if board[ny][nx] == word[i+1]:
                total += dfs(ny,nx, i+1)


    dp[y][x][i] = total
    return total 
    

ans = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == word[0]:
            ans += dfs(y,x,0)
 
print(ans)

