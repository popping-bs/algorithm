import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input= sys.stdin.readline

F,S,G,U,D = map(int, input().split())

visited = [False] * (F+1)

def bfs(start,click):

    q = deque()
    q.append((start,click))
    visited[start] = True
    while q:
        cur , count = q.popleft()

        if cur == G:
            return count 
        
        nxt = cur + U
        if 1 <= nxt <= F and not visited[nxt]:
            visited[nxt] = True
            q.append((nxt,count+1))
        
        nxt = cur - D
        if 1<= nxt <= F and not visited[nxt]:
            visited[nxt] = True
            q.append((nxt,count+1))

    return -1

ans = bfs(S,0)

if ans == -1:
    print("use the stairs")

else:
    print(ans)