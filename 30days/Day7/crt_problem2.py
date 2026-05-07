# 2. Problem: Count Special Pairs (on hold)
# --------------------------------

# Given an array, count pairs (i, j) such that:

# 	i < j
# 	arr[i] + arr[j] is divisible by a given number K
# Input Format:
# 	First line: N
# 	Second line: N integers
# 	Third line: integer K

# Output Format:
# ----------------
# Print count of valid pairs

# Constraints:
# ---------------
# 	1 ≤ N ≤ 2000 (brute-force allowed)

# SOLUTION----------------------------------------------------------------

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

count = 0

for i in range(n):
    for j in range(i+1, n):
        if (arr[i] + arr[j]) % k == 0:
            count += 1

print(count)

