import sys
from collections import deque


sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


n , k = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX +1)

def bfs():

    q = deque()
    q.append(n)
    dist[n] = 0

    while q:
        
        cur = q.popleft()

        if cur == k:
            print(dist[cur])
            break

        for next in (cur-1,cur+1,cur*2):
            if 0<=next<=100000 and dist[next] == -1:
                dist[next] = dist[cur] +1
                q.append(next)

bfs()




        