import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


T = int(input())

for tc in range(1, T+1): 
    N, L  = map(int,input().split())
    food_arr = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [0] * (L+1)

    for score, cal in food_arr:
        for c in range(L, cal-1, -1):
            dp[c] = max(dp[c], dp[c-cal]+score)

    ans = max(dp)

    print(f"#{tc} {ans}")

    
