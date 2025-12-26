import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

T = int(input())


def bfs(a,b):
    #t 마다 dist 새로해야함
    visited = [False] * 10000
    prev = [-1] * 10000
    op   = [''] * 10000

    q = deque([a])
    visited[a] = True

    
    while q:
        cur  = q.popleft()
        if cur == b:
            break
        
        #D
        nxt = (cur * 2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur 
            op[nxt] = 'D'
            q.append(nxt)

        # S
        nxt = 9999 if cur == 0 else cur - 1
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'S'
            q.append(nxt)

        # L
        nxt = (cur % 1000) * 10 + (cur // 1000)
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'L'
            q.append(nxt)

        # R
        nxt = (cur % 10) * 1000 + (cur // 10)
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'R'
            q.append(nxt)

    res = []
    cur = b
    while cur != a:
        res.append(op[cur])
        cur = prev[cur]

    res.reverse()
    return ''.join(res)


for _ in range(T):
    a,b  = map(int, input().split())
    print(bfs(a,b))