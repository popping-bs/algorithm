import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline


N = int(input())
O1,O2 = map(int, input().split())
K = int(input())
NUMS = []
for _ in range(K):
    NUMS.append(int(input()))
print(NUMS)
ans = 2**10

def solve(o1,o2,idx,s):
    global ans
    if idx == K:
        ans = min(ans, s)
        return
    if s > ans:
        return
    t = NUMS[idx]
    solve(t,o2,idx+1, s+abs(t-o1))
    solve(o1,t,idx+1,s+abs(t-o2))

solve(O1,O2,0,0)

print(ans)