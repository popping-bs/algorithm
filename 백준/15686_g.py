import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(N)]

house =[]
chicken = []
for i, row in enumerate(board):
    for j , v in enumerate(row):
        if v == 1:
            house.append((i,j))
        if v == 2:
            chicken.append((i,j))

print(house)
ans =0
def dfs(start, depth):

    if depth == M:
        return
    
    for i in range(start, len(chicken)):
        r = chicken[i][0]
        c = chicken[i][1]
        board[r][c] = 0
        dfs(i+1, depth+1)
        board[r][c] = 2

        