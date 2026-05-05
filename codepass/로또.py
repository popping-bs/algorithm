import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

arr = list(map(int,input().split()))

K = arr[0]
selected = []
def dfs(step):

    if len(selected) == 6:
        print(*selected)
        return 
    

    for i in range(step, K+1):
        selected.append(arr[i])
        dfs(i+1)
        selected.pop()


dfs(1)