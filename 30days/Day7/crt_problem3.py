#3. Problem Name: Wave Array Formation
# --------------------------------

# Given an array of integers of size N, rearrange the elements into a wave-like array.

# An array is said to be in wave form if:

# a1 ≥ a2 ≤ a3 ≥ a4 ≤ a5 ...

# If multiple answers are possible, return the lexicographically smallest wave array.

# Input Format:
# First line contains an integer N — size of the array
# Second line contains N space-separated integers
#  Output Format:
# Print the array in wave form
# Constraints:
# 1 ≤ N ≤ 10⁵
# -10⁹ ≤ array[i] ≤ 10⁹

# SOLUTION-----------------------------------------------------------------------------

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for i in range(0,n-1,2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
