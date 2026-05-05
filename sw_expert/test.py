items = [(10, 100)]
L = 200
dp = [0]*(L+1)

for score, cal in items:
    for c in range(cal, L+1):
        dp[c] = max(dp[c], dp[c-cal]+score)

print(dp[0:201])