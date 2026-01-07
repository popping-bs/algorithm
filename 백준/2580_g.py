import sys 


sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
board = []
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

zeros = [(r,c) for r in range(9) for c in range(9) if board[r][c]==0]
    

def can_put(r,c,v):

    #row
    for j in range(9):
        if board[r][j] == v:
            return False
        
    #col
    for i in range(9):
        if board[i][c] == v:
            return False
        
    sr = (r // 3) * 3
    sc = (c // 3) * 3

    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if board[i][j] == v:
                return False
            
    return True

def dfs(idx):
    if idx == len(zeros):
        for row in board:
            print(*row)
        sys.exit(0)

    r , c = zeros[idx]
    for v in range(1,10):
        if can_put(r,c,v):
            board[r][c] = v
            dfs(idx+1)
            board[r][c] = 0

dfs(0)