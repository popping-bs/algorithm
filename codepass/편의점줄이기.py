import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

apts   = []
stores = []
ans = 10**18 #편의점 거리 총합의 최소값


for row in range(N):
    for col in range(N):
        if board[row][col] == 1:
            apts.append((row,col))
        if board[row][col] == 2:
            stores.append((row,col))



def get_dist(selected_stores):
    res = 0
    for apt in apts:
        dis = 10**18
        for store in selected_stores:
            dis = min(dis, abs(apt[0]-store[0]) + abs(apt[1]-store[1]))
        res+=dis
    return res


def select_store(selected_stores, start_index):
    global ans

    if len(selected_stores) == M:
        ans = min(ans, get_dist(selected_stores))
        return
    for i in range(start_index, len(stores)):
        selected_stores.append(stores[i])
        select_store(selected_stores, i+1)
        selected_stores.pop()


select_store([],0)
print(ans)












                