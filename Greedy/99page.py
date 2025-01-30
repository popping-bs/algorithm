n, k = map(int, input().split())

count = 0
result = n
while True:
    if result == 1:
        break
    else:
        if result%k == 0:
            result = result/k
            count += 1
        else:
            result -= 1
            count += 1

print(count)




n,k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)