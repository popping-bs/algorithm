import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
k = int(input().strip())

for _ in range(k):
    v, e = map (int, input().split())

    graph = [[] for _ in range(v+1)]
    color = [0] * (v+1)


    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bipartite = True

    for start in range(1, v+1):
        if color[start] != 0:
            continue

        q = deque()
        q.append(start)
        color[start] = 1

        while q and bipartite:
            cur = q.popleft()
            for next_node in graph[cur]:
                if color[next_node] == 0:
                    color[next_node] = -color[cur]
                    q.append(next_node)
                else:
                    if color[next_node] == color[cur]:
                        bipartite = False
                        break

    print("YES" if bipartite else "NO")