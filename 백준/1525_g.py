#1525

import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


start = ''.join(''.join(input().split()) for _ in range(3))
target = "123456780"

adj = {
    0: (1, 3),
    1: (0, 2, 4),
    2: (1, 5),
    3: (0, 4, 6),
    4: (1, 3, 5, 7),
    5: (2, 4, 8),
    6: (3, 7),
    7: (4, 6, 8),
    8: (5, 7),
}


def bfs(start_state: str) -> int:
    q = deque([start_state])
    dist = {start_state: 0}

    while q:
        cur = q.popleft()
        if cur == target:
            return dist[cur]
        

        z = cur.index('0') #빈칸 위치 찾음.
        for nz in adj[z]:
            s = list(cur)
            s[z] , s[nz] = s[nz], s[z]
            nxt = ''.join(s)

            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return -1

print(bfs(start)) 