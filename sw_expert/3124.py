import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find(x):
    # 대표(root) 찾기 + 경로 압축(중요!)
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:          # 이미 같은 그룹 -> 사이클
        return False
    parent[rb] = ra       # rb그룹을 ra 밑으로 붙임 (붙이는 방향은 아무거나 OK)
    return True

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))

    edges.sort()

    parent = list(range(V+1))

    ans = 0
    picked = 0

    for w, a, b in edges:
        if union(a, b):
            ans += w
            picked += 1
            if picked == V - 1:
                break

    print(f"#{tc} {ans}")
