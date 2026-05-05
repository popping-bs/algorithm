import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
NUMS = list(map(int,input().split()))
plus, minus, mul, div  = map(int,input().split())


mn = 10**18
mx = -10 ** 18

def div_trunc(a, b):
    # 문제 조건: 음수/양수 나눗셈은 0쪽으로 버림(truncation)
    if a < 0:
        return -((-a) // b)
    return a // b


def dfs(idx, cur, p, m ,x ,d):
    global mn
    global mx

    if idx == N:
        mn = min(mn,cur)
        mx = max(mx,cur)
        return
    nxt = NUMS[idx]

    if p:
        dfs(idx+1, cur + nxt , p-1, m, x ,d)
    if m:
        dfs(idx+1, cur - nxt , p, m-1, x ,d)
    if x:
        dfs(idx+1, cur * nxt , p, m, x-1 ,d)    
    if d:
        dfs(idx+1, div_trunc(cur,nxt) , p, m, x ,d-1)


dfs(1,NUMS[0], plus,minus,mul,div)
print(mx)
print(mn)
            