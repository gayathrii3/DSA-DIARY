# Right Triangle

# * 
# * * 
# * * * 
# * * * * 

# n = int(input())

# for i in range(1, n):
#     for j in range(1, i+1):
#         print('*',end=" ")
#     print()

# -----------------------------------------------------
# Inverted Triangle

# *****
# ****
# ***
# **
# *

# n = int(input())

# for i in range(n):
#     for j in range( n-i):
#         print('*',end="")
#     print()

# -------------------------------------------------
# number triangle

# 1
# 12
# 123
# 1234
# 12345

# n = int(input())

# for i in range(n):
#     for j in range(1, i+1):
#         print(j,end="")
#     print()

# --------------------------------------------------
# Repeated Number Pattern (print i times)

# 1
# 22
# 333
# 4444
# 55555

# n = int(input())

# for i in range(n):
#     for j in range(1, i+1):
#         print(i,end="")
#     print()

# --------------------------------------------------
# Floyd’s Triangle (use count var)

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n = int(input())
# count = 1

# for i in range(1, n+1):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()

# -------------------------------------------------
# pyramid triangle

#     *
#    ***
#   *****
#  *******

# n = int(input())

# for i in range(n):
#     # space
#     for j in range(n - i - 1):
#         print(" ",end="")

#     # star
#     for k in range(i + 1):
#         print("* ",end="")
    
#     print()

# -----------------------------------------------
# Hollow Square

# *****
# *   *
# *   *
# *   *
# *****

# n = 5

# for i in range(n):
#     for j in range(n):

#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")

#     print()

# -----------------------------------------------------------
# diamond pattern

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# n = 5

# for i in range(n):

#     # upper part ---->space
#     for j in range(n - i - 1):
#         print(" ",end="")
#     #------>star
#     for k in range(i + 1):
#         print('* ',end="")

#     print()

#     # lower part----->space
# for i in range(n - 1):
#     for j in range(i + 1):
#         print(" ",end="")

    # for k in range(n - 1 - i):
    #     print("* ",end="")

    # print()

# -------------------------------------------------
# Binary Triangle

# 1
# 01
# 101
# 0101

# n = 4

# for i in range(1, n + 1):

#     for j in range(i):

#         if (i + j) % 2 == 0:
#             print(0, end="")
#         else:
#             print(1, end="")

    # print()