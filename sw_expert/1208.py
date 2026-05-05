import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def solve(total_dump, arr):
    
    for _ in range(total_dump):
        arr.sort()

        if arr[-1] - arr[0] <=1:
            break

        arr[0] +=1 
        arr[-1] -=1 
    arr.sort()
    ans = arr[-1]-arr[0]
    return ans



for tc in range(1, 11):
    
    total_dump = int(input())
    arr = list(map(int, input().split()))

    ans = solve(total_dump, arr)

    print(f"#{tc} {ans}")

    