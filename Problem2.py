n = int(input())
signals = list(map(int, input().split()))
k = int(input())
max_sum = sum(signals[:k])
current_sum = max_sum
for i in range(k, n):
    current_sum = current_sum - signals[i - k] + signals[i]
    max_sum = max(max_sum, current_sum)
print(max_sum)