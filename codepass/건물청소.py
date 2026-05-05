import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


visited = [False] * N
ans = 10**18
selected = []


def calc_diff():
    start_sum = 0
    link_sum = 0
    second_group = []

    for i in range(N):
        for j in range(i+1, N):
            s = board[i][j] + board[j][i]
            if visited[i] and visited[j]:
                start_sum += s
            elif (not visited[i]) and (not visited[j]):
                link_sum += s
        

    return abs(start_sum- link_sum)

def make_group(idx, cnt):
    global ans

    if cnt == N // 2:
        ans = min(ans, calc_diff())
        return
    
    if idx == N:
        return

    if cnt + (N-idx) < N //2:
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            make_group(i+1, cnt+1)
            visited[i] = False

visited[0] = True
make_group(1,1)
print(ans)

