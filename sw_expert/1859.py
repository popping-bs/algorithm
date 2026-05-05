import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())


for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
 
    max_price = 0
    profit = 0

    #[1 5 3 2 4]
    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]

    print(f"#{tc+1} {profit}")