num = list(map(int, input().split()))  #TC = O(n)

smallest = float("inf")
n = len(num)

for i in range(0, n):
    if num[i] < smallest:
        smallest = num[i]

print(f"smallest number:{smallest}")