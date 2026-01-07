#a,b가 결정되면 c 값은 항상 결정 된다.
#state를 a,b로 생각 하자?
#visited[a][b]


from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A,B,C = map(int, input().split())
cap = [A,B,C]
ways = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
visited = [[False] * (B+1) for _ in range(A+1)]

def bfs():
    
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    answer = set()

    while q:
        a, b = q.popleft()
        c = C - a - b
        if a == 0:
            answer.add(c)

        water = [a,b,c]

        for way in ways:
            nw = water[:] #내부 값이 int로 구성되어있으므로 얕은 복사 괜찮
            From = way[0]
            To   = way[1]
            move = min(water[From], cap[To]-water[To])
            if move == 0:
                continue
            nw[From] -= move
            nw[To]+= move
            na, nb = nw[0], nw[1]
            if not visited[na][nb]:
                visited[na][nb] = True
                q.append((na,nb))

    return sorted(answer)


print(*bfs())

