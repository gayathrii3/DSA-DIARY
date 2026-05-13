# print 1 to 100 using for loop

# for i in range(1, 100, 1):
#     print(i)

# ---------------------------------------------------
# print 100 to 1

# for i in range(100, 0, -1):
#     print(i)

# ---------------------------------------------------
# print mul of n

# n = int(input())

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# ----------------------------------------------------
# sum of first n nums(while loop)

# n = int(input())
# sum = 0

# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print(sum)

# ---------------------------------------------------
# factorial of n

# n = int(input())
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print(fact)

# ----------------------------------------------------
# Reverse a string using for loop

# word = "Gayathri"
# rev = ""

# for w in range(len(word)-1, -1, -1):
#     rev += word[w]

# print(rev)

# ----------------------------------------------------
# Find largest element in a list

# nums = [4, 18, 2, 9, 1]
# large = nums[0]

# for n in nums:
#     if n > large:
#         large = n

# print(large)

# ---------------------------------------------------
# Count frequency of characters

# word = "Gaaaayaa"
# freq = {}

# for ch in word:
#     if ch not in freq:
#         freq[ch] = 1
#     else:
#         freq[ch] += 1

# print(freq)

# --------------------------------------------------
# Find second largest element

# nums = [12, 45, 6, 89, 23]
# largest = sec_largest = float('-inf')

# for n in nums:
#     if n > largest:
#         sec_largest = largest
#         largest = n

#     elif n > sec_largest and n != largest:
#         sec_largest = n

# print(f"largest = {largest}\nsec largest = {sec_largest}") 

# ---------------------------------------------------
# Find common elements in two lists

# a = [1,2,3,4]
# b = [3,4,5,6]

# common = []

# for i in a:
#     if i in b:
#         common.append(i)

# print(common)