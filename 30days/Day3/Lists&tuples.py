#************** Lists and Tuples***************

# Find largest element in a list

# n = [12, 23, 34, 45, 56]
# largest = n[0]

# for i in n:
#     if i > largest:
#         largest = i

# print(largest)

# -------------------------------------------------
# Find smallest element

# num = [2,5,1,7,34,8.9,0.4]
# smallest = num[0]

# for n in num:
#     if n < smallest:
#         smallest = n

# print(smallest)

# -------------------------------------------------
# even and odd numbers

# num = [23,2,45,6,8,9,7,41]
# even = []
# odd = []

# for n in num:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)

# print(f"even = {even}\n odd = {odd}")

# -------------------------------------------------
# Reverse a list (without using reverse())

# num = [9, 8, 7, 6, 5]
# reverse = []

# for n in range(len(num)-1, -1, -1):
#     reverse.append(num[n])

# print(reverse)

# ------------------------------------------------
# Check element exists

# x = int(input())
# num = [9, 4, 5, 2]

# if x in num:
#     print(f"{x} found at {num.index(x)}")
# else:
#     print(f"{x} not found")

# ------------------------------------------------
# Find second largest element

# num = [12,34,45,67,32]
# largest = num[0]
# sec_largest = 0

# for n in num:
#     if n > largest:
#         sec_largest = largest
#         largest = n
#     elif n > sec_largest and n != largest:
#         sec_largest = n

# print(largest,sec_largest)

# ----------------------------------------------------
# Remove duplicates

# num = [2,3,1,2,3,5,6,2,6]
# dup = []

# for n in num:
#     if n not in dup:
#         dup.append(n)
# print(dup)

# ------------------------------------------------------
# Move zeros to end
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# nums = [0, 1, 0, 3, 12]
# result = []

# for n in nums:
#     if n != 0:
#         result.append(n)
# result += [0] * nums.count(0)   # counts the no. of zeroes

# print(result)

# ------------------------------------------------------------

# Find second smallest element

# nums = [2, 5, 8, 9, 1, 0]
# smallest = second_smallest = float('inf')

# for n in nums:
#     if n < smallest:
#         second_smallest = smallest
#         smallest = n

#     elif n < second_smallest and n != smallest:
#         second_smallest = n

# print(smallest,second_smallest)

# --------------------------------------------
# find duplicates

# num = [2,3,3,4,5,6,6,1]

# seen = set()
# dup = set()

# for n in num:
#     if n not in seen:
#         seen.add(n)
#     else:
#         dup.add(n)

# print(seen,"\n",dup)

# ---------------------------------------------
# Rotate list by k

# num = [1,2,3,4,5,6]
# k = 3

# result = num[-k:len(num)] + num[:-k]

# print(result)

# -------------------------------------------------------
# ************************tuple***************************
# -------------------------------------------------------

# tup = (1, 2, 3, 4)
# print(tup.index(2))
# print(tup.count(2))

# ----------------------------------------------------

# movies = []

# mov = input("Enter 1st movie:")
# movies.append(mov)
# mov = input("Enter 2nd movie:")
# movies.append(mov)
# mov = input("Enter 3rd movie:")
# movies.append(mov)

# print(movies)

# -----------------------------------------------------

# check palindrome

# num1 = [1,1,2,2,1,0]
# num2 = num1.copy()
# num2.reverse()

# if num1 == num2:
#     print("palindrome")
# else:
#     print("not palindrome")

#------------------------------------------------------
# Find max & min in tuple (without max/min)

# tup = (2, 4, 6, 7, 3, 9)
# max = float('-inf')
# min = float('inf')

# for n in tup:
#     if n > max:
#         max = n
#     if n < min:
#         min = n
# print("max =",max,"min = ",min)

# ------------------------------------------------------
# Merge two lists and remove duplicates

# list1 = [1, 2, 3, 4]
# list2 = [2, 6, 3, 8]

# list1.extend(list2)   # merge lists

# result = set(list1)   # remove duplicates

# print(result)
