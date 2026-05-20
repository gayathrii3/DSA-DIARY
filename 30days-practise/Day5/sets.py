# set1 = {1, 2, 3, 4}
# set2 = {2, 4, 6, 7, 5}
# print(set1.intersection(set2))  #common values(&)

# ----------------------------------------------

# set1 = {1, 2, 3, 4}
# set2 = {2, 4, 6, 7, 5}
# print(set1.union(set2))  #unique values

# ----------------------------------------------
# Remove duplicates from list

# num = [1, 2, 2, 3, 4, 4]
# dup = set()

# for n in num:
#     if n not in dup:
#         dup.add(n)

# print(dup)

# ---------------------------------------------
# Find common elements(without intersection)

# A = [1,2,3,4]
# B = [3,4,5,6]

# common = set()

# for n in A:
#     if n in B:
#         common.add(n)

# print(common)

# ----------------------------------------------
# Check if two lists have any common element

# A = [1,2,3]
# B = [5,6,3]

# for n in A:
#     if n in B:
#         print("Yes")
#         break
# else:
#     print("all are unique values")

# ----------------------------------------------
# Find unique pairs with given sum

# nums = [1,2,3,4,5]
# target = 6

# unique = set()

# for n in nums:
#     if target - n in unique:
#         print((target - n, n))
#     unique.add(n)