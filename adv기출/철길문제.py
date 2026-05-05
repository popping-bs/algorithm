import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline()


T = int(input())


for i in range(T):

    N,M,R = map(int, input().split())


    node ={}
    for i in range(N+1):
        node[i] = []

    for line in range(M):
        a,b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)


    def bfs(start):
        visited = [False] * (N+1)
        count = 0
        q = deque()
        q.append(start)
        visited[start] = True
        while q:

            now = q.popleft()
            nxt_points = node[now]

            for nxt in nxt_points:
                if not visited[nxt]:
                    visited[nxt] = True
                    count +=1
                    q.append(nxt)

        return count

    ans = 0
    def dfs(start, count):
        global ans
        if count == R:
            for home in range(1,N+1):
                val = bfs(home)
                ans = max(ans, val)
        for i in range(start, N+1):
            for j in range(i+1, N=1):
                if j not in node[i] and i not in node[j]:
                    node[i].append(j)
                    node[j].append(i)
                    dfs(i+1, count+1)
                    node[i].pop()
                    node[j].pop()


    dfs(1,0)
    print(ans)