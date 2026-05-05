import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline



for tc in range(10):
    N = int(input())
    building_heights = list(map(int, input().split()))
    total = 0

    for i in range(2, N-2):
        left1 = building_heights[i]-building_heights[i-1]
        left2 = building_heights[i]-building_heights[i-2]
        right1 = building_heights[i]-building_heights[i+1]
        right2 = building_heights[i]-building_heights[i+2]

        if left1 > 0 and left2 > 0 and right1 > 0 and right2 > 0:
            visible_count = min(left1, left2, right1, right2)
            total += visible_count


    print(f"#{tc} {total}")