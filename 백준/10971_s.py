import sys


sys.stdin = open('input.txt', 'r')


input = sys.stdin.readline

n = int(input())

#visited = [[False] * n for i in range(n)]
visited = [False] * n
w = [list(map(int, input().split())) for _ in range(n)]

INF = 10**15
ans = INF



def dfs(start:int, cur:int, cnt:int, cost:int):

    global ans


    if cost >= ans:
        return
    
    if cnt == n:
        if w[cur][start] != 0:
            ans = min(ans , cost + w[cur][start])
        return
    

    for nxt in range(n):
        if not visited[nxt] and w[cur][nxt] !=0:
            visited[nxt] = True
            dfs(start, nxt , cnt + 1 , cost + w[cur][nxt])
            visited[nxt] = False
start = 0 
visited[start] = True
dfs(start, start , 1 , 0)

print(ans)
