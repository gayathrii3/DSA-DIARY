num = list(map(int, input().split()))  #TC = O(n)

largest = float("-inf")
n = len(num)

for i in range(0, n):
    if num[i] > largest:
        largest = num[i]

print(f"Largest number:{largest}")