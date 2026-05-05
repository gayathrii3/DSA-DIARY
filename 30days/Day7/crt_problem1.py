# 1. Problem Name: Move All Zeros to End
# --------------------------------------

# You are given an array of integers of size N. Your task is to move all the zeros in the array to the end while maintaining the relative order of the non-zero elements.

# Input Format:
# First line contains an integer N — size of the array
# Second line contains N space-separated integers
# Output Format:
# Print the modified array after moving all zeros to the end
# Constraints:
# 1 ≤ N ≤ 10⁵
# -10⁹ ≤ array[i] ≤ 10⁹

# SOLUTION-------------------------------------------------------------------------------------------------------------------------------------

n = int(input())
arr = list(map(int, input().split()))

non_zero = []

for i in range(n):
    if arr[i] != 0:
        non_zero.append(arr[i])

result = non_zero + [0] * arr.count(0)

print(result)
