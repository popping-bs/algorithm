n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0 

'''while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second 
    m -= 1
'''
#시간복잡도 줄인 버전.
count =  int(m/(k+1)) * k
count += m%(k+1)
result = 0

result += count * first
result += (m-count) * second


print(result)
