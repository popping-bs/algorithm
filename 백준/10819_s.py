import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())
array_list = list(map(int, input().split()))

visited = [False] * n
selected = [0] * n
answer = 0


def calc_value(seq):
    total = 0 
    for i in range(n-1):
        total += abs(seq[i]- seq[i+1])
    return total

def dfs(depth):

    global answer

    if depth == n:
        value = calc_value(selected)
        if value > answer:
            answer = value
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            selected[depth] = array_list[i]
            dfs(depth+1)
            visited[i] = False    

dfs(0)
print(answer)
