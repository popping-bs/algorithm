import sys
from collections import deque



sys.stdin = open('input.txt', 'r')

n, m, v = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
stack = []

for _ in range(m):
    a,b =  map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for new_node in graph[node]:
        if not visited[new_node]:
            dfs(new_node)

dfs(v)
print()

visited2 = [False] * (n+1)
def bfs(node):
    visited2[node] = True
    q = deque()
    q.append(node)
    print(node, end=' ')
    while q:
        a = q.popleft()
        for new_node in graph[a]:
            if not visited2[new_node]:
                visited2[new_node] = True
                q.append(new_node)
                print(new_node, end=' ')

bfs(v)