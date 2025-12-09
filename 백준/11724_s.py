import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


def bfs(node):
    visited[node] = True
    q = deque()
    q.append(node)
    while q:
        a = q.popleft()
        for new_node in graph[a]:
            if not visited[new_node]:
                visited[new_node] = True
                q.append(new_node)

cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt +=1


print(cnt)
