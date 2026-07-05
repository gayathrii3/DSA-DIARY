num = list(map(int, input().split()))  #TC = O(n)

largest = sec_largest = float("-inf")
n = len(num)

for i in range(0, n):
    if num[i] > largest:
        sec_largest = largest
        largest = num[i]

    elif num[i] > sec_largest and num[i] != largest:
        sec_largest = num[i]

print(f"Second largest:{sec_largest}")